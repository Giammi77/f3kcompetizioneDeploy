# -*- coding: utf-8 -*-
from gnr.core.gnrdecorator import public_method


class GnrCustomWebPage(object):
    py_requires = 'th/th:TableHandler'
    css_requires='f3k_mobile'

    def main(self,pane,**kwargs):     

        main_bc=pane.borderContainer(datapath='managment')
        contest_director_id,full_name = self.db.table('contest.contest_director'
                                    ).readColumns(columns='$id,$full_name',
                                                where='$user_id=:uid',
                                                uid=self.rootenv['user_id'])
        main_bc.data('.current_full_name', full_name)
        main_bc.data('.contest_director_id', contest_director_id)

        self.mainToolbar(main_bc.contentPane(region='top'))

        bc=main_bc.borderContainer(region='center')
        top=bc.contentPane(region='top',height='10%')
        center=bc.contentPane(region='center')
        fb=top.formbuilder(cols=2)
        
        fb.dbselect(value='^.competition',
                    width='15em',
                    dbtable='f3kp.competition',
                    lbl='!![en]Select Competition',
                    hasDownArrow=True,
                    condition="$contest_director_id=:contest_director_id AND $state_code=:code",
                    condition_contest_director_id='^.contest_director_id',
                    condition_code='S')
        fb.div('^.count_down',lbl='!![en]Time Remaining: ')
        center.inlineTableHandler(table='f3kp.managment', 
                                datapath='managment',
                                viewResource='ViewFromContestPageMobile',
                                condition='$competition_id=:id',
                                condition_id='^managment.competition',
                                condition_onStart=True,
                                liveUpdate=True,autoSave=True)

        # main_bc.dataRpc('.time_end',self.time_end,competition_id='^.competition')
        main_bc.data('.count_down','')
        main_bc.data('.running',True)
        main_bc.data('.current_time',True)
        main_bc.data('.finish','')
        main_bc.dataController("""
                                var finish = new Date(time_end);
                                genro.setData('managment.finish',finish);
                                
                                """,_onStart=True,time_end='^.time_end')
        main_bc.dataController("""
                                var current_time = new Date();
                                genro.setData('managment.current_time',current_time);

                                """,_timing=1,_onStart=True)
        main_bc.dataController("""   
                                if(running){var end_task=new Date(finish);
                                            var now = new Date();
                                            var countDown= parseInt((end_task-now)/1000);
                                            console.log(countDown);
                                            if (countDown<0 || isNaN(countDown)){
                                                            genro.setData('managment.count_down','00:00');return};
                                            if (countDown==0){
                                                            genro.setData('managment.count_down','00:00');}
                                                        
                                                        else{
                                                            var minutes= parseInt(countDown/60);
                                                            var seconds= countDown-(minutes*60);
                                                            var display= minutes+':'+seconds;
                                                            genro.setData('managment.count_down',display);
                                                            }
                                            }
        
                            """,_timing=1,running='^.running',finish='=.finish',_onStart=True)
        main_bc.dataController('''
                                if (count_down == '00:00'){
                                    genro.setData('managment.search_time_end',true);
                                }
                                else{
                                    genro.setData('managment.search_time_end',false)
                                }
                                ''',running='^.running',_timing=1,count_down='=.count_down')

        main_bc.dataRpc('.time_end',self.time_end,competition_id='=.competition',
                        search_time_end='^.search_time_end',_timing=1) 


    @public_method
    def time_end(self,competition_id=None,search_time_end=None):
        try:
            time_end=self.db.table('f3kp.managment'
                                        ).readColumns(columns='$time_end',
                                                    where='$competition_id=:competition_id AND $activated=:activated',
                                                    competition_id=competition_id,
                                                    activated=True
                                                    )
            return time_end
        except:
            time_end= None
            return 
        

    def mainToolbar(self,pane):
        bar = pane.slotToolbar('2,pageTitle,*,logoutButton,2')
        bar.pageTitle.div('^.current_full_name',font_weight='bold')
        bar.logoutButton.button('Logout',action='genro.logout();')