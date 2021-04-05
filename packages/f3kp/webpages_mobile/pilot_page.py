# -*- coding: utf-8 -*-
from gnr.core.gnrdecorator import public_method
import time


class GnrCustomWebPage(object):
    py_requires = 'th/th:TableHandler'
    css_requires='f3k_mobile'

    def main(self,pane,**kwargs):

        pilot_id,full_name = self.db.table('f3kp.pilot'
                            ).readColumns(columns='$id,$full_name',
                                            where='$user_id=:uid',
                                            uid=self.rootenv['user_id'])
        try:
            competition_id = self.db.table('f3kp.registration'
                                        ).readColumns(columns='$competition_id',
                                                    where='$pilot_id=:pilot_id AND $competition_state_code=:code',
                                                    pilot_id=pilot_id,
                                                    code='S')
        except:
            competition_id=None
        pane.data('current_pilot_id', pilot_id)
        pane.data('current_full_name', full_name)
        if not competition_id:
            self.registering_page(pane)
            return
        
        main_bc=pane.borderContainer()
        main_bottom=main_bc.contentPane(region='top', height='5%')
     
        tb=main_bc.tabContainer(region='center',tabPosition="top",selectedPage='^entry.selectedPage',_class='tab_mobile')
        
        bc = tb.borderContainer(title='ENTRY',datapath='entry',pageName='entryFlightTimes')
        tc_pilot_views=tb.tabContainer(title='RESULTS',tabPosition ='top',selectedPage='^entry.selectedResults',pageName='results')
        
        top=bc.contentPane(region='top',height='12%')                                   # top bars to show data user information
        center=bc.contentPane(region='center',font_size='15px',text_align='center')                                          # grid to show flight time already inserted
        bottom=bc.contentPane(region='bottom', height='54%')                            # gui for show and edit flight time
        b_bc=bottom.borderContainer()                                                   # display and buttons

        try:
            combination_id_for_entry_time= self.db.table('f3kp.combination'
                                        ).readColumns(columns='$id',
                                                    where='$pilot_id=:pid AND $managment_activated=:managment_activated',
                                                    pid=pilot_id,
                                                    managment_activated=True
                                                    )

        except:
            combination_id_for_entry_time=None

        try: 
            current_combination_id,combination_name,task_description=self.db.table('f3kp.combination'
                                        ).readColumns(columns='$id,$combination_name,$task_description',
                                                    where='$competition_id=:competition_id AND $managment_activated=:managment_activated',
                                                    competition_id=competition_id,
                                                    managment_activated=True
                                                    )
        except:
             current_combination_id,combination_name,task_description=None,None,None

        try:
            time_end=self.db.table('f3kp.managment'
                                        ).readColumns(columns='$time_end',
                                                    where='$competition_id=:competition_id AND $activated=:activated',
                                                    competition_id=competition_id,
                                                    activated=True
                                                    )
        except:
            time_end= None

        # bc.data('.current_pilot_id', pilot_id)
        # bc.data('.current_full_name', full_name)

        bc.data('.current_competition_id', competition_id)  

        bc.data('.combination_id_for_entry',combination_id_for_entry_time)

        bc.data('.current_combination', current_combination_id)
        bc.data('.combination_name', combination_name)
        bc.data('.task_description',task_description)

        bc.data('.time_end',time_end)
        
        bc.data('.count_down','')
        bc.data('.running',True)
        bc.data('.current_time',True)
        bc.data('.finish','')


        # THIS DATACONTROLLER USED TO FORMAT END TIME OF THE CURRENT TASK

        bc.dataController("""
                                var finish = new Date(time_end);
                                genro.setData('entry.finish',finish);
                                
                                """,_onStart=True,time_end='^.time_end')

        bc.dataController("""
                                var current_time = new Date();
                                genro.setData('entry.current_time',current_time);

                                """,_timing=1,_onStart=True)
        
        bc.dataController("""   
                                if(running){var end_task=new Date(finish);
                                            var now = new Date();
                                            var countDown= parseInt((end_task-now)/1000);
                                            if (countDown<0 || isNaN(countDown)){
                                                            genro.setData('entry.count_down','00:00');return};
                                            if (countDown==0){
                                                            genro.setData('entry.running',false);
                                                            genro.setData('entry.count_down','00:00');}
                                                        
                                                        else{
                                                            var minutes= parseInt(countDown/60);
                                                            var seconds= countDown-(minutes*60);
                                                            var display= minutes+':'+seconds;
                                                            genro.setData('entry.count_down',display);
                                                            }
                                            }
        
                            """,_timing=1,running='^.running',finish='=.finish',_onStart=True)
        




        # THIS DATACONTROLLER USED FOR KEEP UPDATE THE DATA BETWEEN TABS
        bc.dataController("""var competition_id= genro.getData('entry.current_competition_id');
                            genro.setData('entry.current_competition_id','');
                            genro.setData('entry.current_competition_id',competition_id);
                        """
                            ,fire='^.selectedResults',fire_2='^.selectedPage')

        self.logoutToolbar(top)
        self.entryToolbar(top)
        self.pilot_views(tc_pilot_views)
        self.time_remaining(main_bottom,'^entry.count_down')
        # if not competition_id:
        #     self.message(center,'THERE IS NO COMPETITION AVAILABLE')
        #     return

        tb.contentPane(title='TASKS').plainTableHandler(table='f3kp.managment', 
                                datapath='managment',
                                viewResource='ViewFromPilotPageMobile',
                                condition='$competition_id=:competition_id',
                                condition_competition_id=competition_id,
                                condition_onStart=True,
                                liveUpdate=True,autoSave=True)

        if not combination_id_for_entry_time :
            
            self.message(center,'ENTRY TIME NOT AVAILABLE, YOU ARE NOT IN THIS TASK')
            return
        
        self.flight_time_view(center)
        self.show_edit_time(b_bc.contentPane(region='top',width='100%',height='25%'))
        self.entry_time(b_bc.contentPane(region='center'))

        bc.dataController("""
                            if(row_count){
                                this.setRelativeData('.number_flight_time',row_count.toString());
                                if(time!=0){
                                    this.setRelativeData('.minutes',''+minutes);
                                    this.setRelativeData('.seconds',''+seconds);
                                    this.setRelativeData('.tenths',''+tenths);
                                }
                                else {
                                this.setRelativeData('.minutes','-');
                                this.setRelativeData('.seconds','-');
                                this.setRelativeData('.tenths','-');
                                }
                            }
                            else{
                                this.setRelativeData('.number_flight_time','N');
                                this.setRelativeData('.minutes','-');
                                this.setRelativeData('.seconds','-');
                                this.setRelativeData('.tenths','-');
                            };
                            """, row_count='^.selected_row_count',
                            minutes='^.selected_minutes', seconds='^.selected_seconds',tenths='^.selected_tenths',
                            time='^.selected_flight_time')

    def time_remaining(self,cp,time):
        table=cp.table(margin='auto')
        tbody=table.tbody()
        row=tbody.tr(_class='time_remaing')
        cel=row.td()
        cel.div("TIME REMAINING:")
        cel=row.td()
        cel.div(time,text_align='right',width='3em')

    def flight_time_view(self,center):
        center.inlineTableHandler(table='f3kp.flight_time',
                        viewResource='ViewFromPilotMobile',
                        datapath='flight_time', 
                        nodeId='flight_time', 
                        condition='@combination_id.pilot_id=:pid AND @combination_id.@competition_task_id.@managment.activated=:activated',
                        condition_pid='^current_pilot_id',
                        condition_activated=True,
                        pbl_classes=False,condition_onStart=True,
                        font_size = '25px',
                        searchOn=False,
                        addrow=False,
                        delrow=True,
                        border='1px solid gray',
                        grid_selected_id='entry.selected_flight_time_id',
                        grid_selected__row_count='entry.selected_row_count',
                        grid_selected_minutes='entry.selected_minutes',
                        grid_selected_seconds='entry.selected_seconds',
                        grid_selected_tenths='entry.selected_tenths',
                        grid_selected_flight_time='entry.selected_flight_time'
                        )

    def show_edit_time(self,cp):
        cp.data('.minutes','-')
        cp.data('.seconds','-')
        cp.data('.tenths','-')
        cp.data('.selected_','selected_')
        cp.data('.number_flight_time','N')


        time_table=cp.table(margin=0,margin_top='0',width='100%',_class='^.selected_') # il margin imposta un equo spazio a sinistra e a destra del bo
        tbody=time_table.tbody(align='center',font_size='12px')

        row=tbody.tr()

        cel=row.td()
        cel.div()

        cel=row.td()
        cel.div('MINUTES')
        cel=row.td()
        cel.div('SECONDS')
        cel=row.td()
        cel.div('TENTHS')

        row=tbody.tr(font_size='40px')
        cel=row.td()
        cel.div('^.number_flight_time',padding_right='6px',padding_left='6px',
                  font_size='15px')
        cel=row.td()
        cel.div('^.minutes',padding_right='6px',padding_left='6px',_class='minutes',
                  connect_touchstart="genro.setData('entry.selected_','selected_minutes')")

        cel=row.td()
        cel.div('^.seconds',padding_right='6px',padding_left='6px',_class='seconds',
                  connect_touchstart="genro.setData('entry.selected_','selected_seconds')")
        cel=row.td()
        cel.div('^.tenths',padding_right='6px',padding_left='6px',_class='tenths',
                  connect_touchstart="genro.setData('entry.selected_','selected_tenths')")

    def entry_time(self,cp):
        time_table=cp.table(margin='auto',_class='btn_digit')
        tbody=time_table.tbody()
       
        row=tbody.tr()
        cel=row.td()
        cel.button('7',action="genro.publish('insertDigit',{digit:7,selected_:'.selected_'})")
        cel=row.td()
        cel.button('8',action="genro.publish('insertDigit',{digit:8,selected_:'.selected_'})")
        cel=row.td()
        cel.button('9',action="genro.publish('insertDigit',{digit:9,selected_:'.selected_'})")
        cel=row.td()
        cel.button('-',action="genro.publish('removeDigit',{selected_:'.selected_'})")


        row=tbody.tr()
        cel=row.td()
        cel.button('4',action="genro.publish('insertDigit',{digit:4,selected_:'.selected_'})")
        cel=row.td()
        cel.button('5',action="genro.publish('insertDigit',{digit:5,selected_:'.selected_'})")
        cel=row.td()
        cel.button('6',action="genro.publish('insertDigit',{digit:6,selected_:'.selected_'})")
        cel=row.td()
        cel.button('+',action="""genro.publish('saveTime',{minutes:'^.minutes',seconds:'^.seconds',tenths:'^.tenths',
                                selected_flight_time_id:'^.selected_flight_time_id'});genro.publish('aggiorna_selezione') """)


        row=tbody.tr()
        cel=row.td()
        cel.button('1',action="genro.publish('insertDigit',{digit:1,selected_:'.selected_'})")
        cel=row.td()
        cel.button('2',action="genro.publish('insertDigit',{digit:2,selected_:'.selected_'})")
        cel=row.td()
        cel.button('3',action="genro.publish('insertDigit',{digit:3,selected_:'.selected_'})")
        cel=row.td()
        cel.button('0',action="genro.publish('insertDigit',{digit:0,selected_:'.selected_'})")
        cel=row.td()   

        cp.dataController("""this.setRelativeData('.minutes','-');
                            this.setRelativeData('.seconds','-');
                            this.setRelativeData('.tenths','-');
                            this.setRelativeData('.selected_','selected_');
                            
                         """,fire='^.clear_display')

        cp.dataRpc('.clear_display',self.addTime,combination_id='=.combination_id_for_entry',subscribe_saveTime=True,
                    _lockScreen=dict(message='Registering time'))
        
        cp.script("""var digit_manager = {
            store : function(path_to_store,digit){

                var _stored=genro.getData(path_to_store);
                if (_stored.length==2){return _stored;}
                if (_stored=='-'){_stored=''};
                return _stored+digit;
                },

            store_tenths : function(path_to_store,digit){

                var _stored=genro.getData(path_to_store);
                if (_stored=='-'){_stored=''};
                if (_stored.length==1){return _stored;}
                return _stored+digit;
                },

            remove : function(path_to_remove){
                var _stored=genro.getData(path_to_remove);
                if (_stored=='-'){return _stored;}
                if (_stored.length==1){return '-';}
                return _stored.slice(0,-1);
                }
            }
        
                    """)

        cp.dataController("""var stored=this.getRelativeData(selected_);
                            if (stored=='selected_minutes'){this.setRelativeData('.minutes',digit_manager.store('entry.minutes',digit))}
                            if (stored=='selected_seconds'){this.setRelativeData('.seconds',digit_manager.store('entry.seconds',digit))}
                            if (stored=='selected_tenths'){this.setRelativeData('.tenths',digit_manager.store_tenths('entry.tenths',digit))}
                            """,subscribe_insertDigit=True)

        cp.dataController("""var stored=this.getRelativeData(selected_);
                            if (stored=='selected_minutes'){this.setRelativeData('.minutes',digit_manager.remove('entry.minutes'))}
                            if (stored=='selected_seconds'){this.setRelativeData('.seconds',digit_manager.remove('entry.seconds'))}
                            if (stored=='selected_tenths'){this.setRelativeData('.tenths',digit_manager.remove('entry.tenths'))}
                            """,subscribe_removeDigit=True)

        cp.dataController("""var pilot_id= genro.getData('current_pilot_id');
                                    genro.setData('current_pilot_id','');
                                    genro.setData('current_pilot_id',pilot_id);
                                """
                                    ,subscribe_aggiorna_selezione=True)

    @public_method
    def addTime(self,combination_id,**kwargs):
        tbl_flight_time=self.db.table('f3kp.flight_time')
        # into kwargs : minutes,seconds,tenths,selected_flight_time_id

        try:
            flight_time=int(kwargs['minutes'])*60
        except:
            flight_time=0
        try:
            flight_time+=int(kwargs['seconds'])
        except:
            flight_time+=0

        try:
            flight_time+=int(kwargs['tenths'])/10
            
        except:
            flight_time+=0
        
        if not kwargs['selected_flight_time_id']: #try to save new flight_time
            tbl_flight_time.add_flight_time(combination_id,flight_time)
            return


        #else update existing
        tbl_flight_time.update_flight_time(kwargs['selected_flight_time_id'],flight_time)


    def logoutToolbar(self,pane):
        bar = pane.slotToolbar('2,pageTitle,*,logoutButton,2',childname='upper',_class='slotbar_logout')
        bar.pageTitle.div('^current_full_name',font_weight='bold')
        bar.logoutButton.button('Logout',action='genro.logout();')

    def entryToolbar(self,pane):
        # font_size_top_bars2= '11px'
        # font_size_top_bars3= '11px'
        bar2 = pane.slotToolbar('*,combination,*',childname='lower',_position='>upper',_class='slotbar_entry')
        bar2.combination.div('^.combination_name',font_weight='bold')
        bar3 = pane.slotToolbar('*,task,*',childname='lower_lower',_position='>lower',_class='slotbar_entry')
        bar3.task.div('^.task_description',font_weight='bold')

    def message(self,pane,message=None):
        pane.div(message,font_size='15px',text_align='center')

    

    def pilot_views(self,tc):

        tc.contentPane(title='ROUNDS',pageName='rounds').plainTableHandler(table='f3kp.combination',datapath='combination',
                                        title='Combinations',
                                        viewResource='View_from_pilot_mobile',
                                        condition="$competition_id=:id",
                                        condition_id='^entry.current_competition_id',
                                        condition_onStart=True,
                                        font_size = '13px',
                                        )
            
        tc.contentPane(title='RANKING',pageName='ranking').plainTableHandler(table='f3kp.registration',
                                        title='Ranking',
                                        datapath='ranking',
                                        viewResource='ViewFromRanking',
                                        condition="$competition_id=:id",
                                        condition_id='^entry.current_competition_id',
                                        condition_onStart=True,
                                        font_size = '15px',
                                        grid_showLineNumber=True
                                        )
    def registering_page(self,pane):
        main_bc=pane.borderContainer()
     
        tb=main_bc.tabContainer(region='center',tabPosition="top",selectedPage='^mycompetition.selectedPage',_class='tab_mobile')
        
        bc = tb.borderContainer(title='MY COMPETITION',datapath='mycompetition',pageName='mycompetition')
        top=bc.contentPane(region='top',height='6%')
        center=bc.contentPane(region='center',text_align='center')                                          # grid to show flight time already inserted
        
        cp=tb.contentPane(title='REGISTERING')

        self.logoutToolbar(top)
        self.myCompetition(center)
        self.registeringCompetition(cp)
        
    def myCompetition(self,cp):
        cp.dialogTableHandler(table='f3kp.competition',
                                viewResource='ViewFromPilotMobile',
                                formResource='Form_from_pilot_mobile',
                                condition='@registration.pilot_id=:pr_pilot_id',
                                condition_pr_pilot_id='^current_pilot_id',
                                condition_onStart=True,
                                addrow=False,delrow=False,
                                liveUpdate=True) 
    
    def registeringCompetition(self,cp):
        cp.plainTableHandler(table='f3kp.competition',
                                datapath='main.competition',
                                viewResource='ViewFromRegisteringMobile',
                                condition_onStart=True)