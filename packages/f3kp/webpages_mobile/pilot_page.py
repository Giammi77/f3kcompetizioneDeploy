# -*- coding: utf-8 -*-
from gnr.core.gnrdecorator import public_method



class GnrCustomWebPage(object):
    py_requires = 'th/th:TableHandler'
    css_requires='f3k'



    def main(self,pane,**kwargs):

        ################################
        # TO DO preference for mobile

        show_edit_flight_time_pane ='63%'
        height_display_entry_time = '22%'
        tb=pane.tabContainer(tabPosition="top")

        bc = tb.borderContainer(title='ENTRY FLIGHT TIMES',datapath='entry')
        tc_pilot_views=tb.tabContainer(title='RESULTS',tabPosition ='top')
        top=bc.contentPane(region='top')                                                # top bars to show data user information
        center=bc.contentPane(region='center')                                          # grid to show flight time almost inserted
        bottom=bc.contentPane(region='bottom', height=show_edit_flight_time_pane)       # gui for show and edit flight time
        b_bc=bottom.borderContainer()                                                   # display and buttons
        
        pilot_id,full_name = self.db.table('f3kp.pilot'
                                    ).readColumns(columns='$id,$full_name',
                                                  where='$user_id=:uid',
                                                 uid=self.avatar.user_id)
        try:
            competition_id = self.db.table('f3kp.registration'
                                        ).readColumns(columns='$competition_id',
                                                    where='$pilot_id=:pilot_id AND $competition_state_code=:code',
                                                    pilot_id=pilot_id,
                                                    code='S')
        except:
            competition_id=None
        
        try:
            combination_id_for_entry_time= self.db.table('f3kp.combination'
                                        ).readColumns(columns='$id',
                                                    where='$pilot_id=:pid AND $competition_task_state_code=:state',
                                                    pid=pilot_id,
                                                    state='S'
                                                    )
        except:
            combination_id_for_entry_time=None

        try:
            current_combination_id,combination_name,task_description=self.db.table('f3kp.combination'
                                        ).readColumns(columns='$id,$combination_name,$task_description,',
                                                    where='$competition_id=:competition_id AND $competition_task_state_code=:state',
                                                    competition_id=competition_id,
                                                    state='S'
                                                    )
        except:
             current_combination_id,combination_name,task_description=None,None,None

        bc.data('.current_pilot_id', pilot_id)
        bc.data('.current_full_name', full_name)
        bc.data('.current_competition_id', competition_id)  
        bc.data('.current_combination', current_combination_id)
        bc.data('.combination_id_for_entry',combination_id_for_entry_time)
        bc.data('.combination_name', combination_name)
        bc.data('.task_description',task_description)

        self.logoutToolbar(top)
        self.entryToolbar(top)
        self.pilot_views(tc_pilot_views)

        if not competition_id:
            self.message(center,'THERE IS NOT COMPETITION AVAILABLE')
            return

        if not combination_id_for_entry_time :
            self.message(center,'ENTRY TIME NOT AVAILABLE, YOU ARE NOT IN THIS TASK')
            return

        self.flight_time_view(center)
        self.show_edit_time(b_bc.contentPane(region='top',width='100%',height=height_display_entry_time))
        self.entry_time(b_bc.contentPane(region='center'))

        bc.dataController("""
                            if(row_count){
                                this.setRelativeData('.number_flight_time',row_count.toString());
                                this.setRelativeData('.minutes',''+minutes);
                                this.setRelativeData('.seconds',''+seconds);
                                this.setRelativeData('.tenths',''+tenths);
                                }
                            else{
                                this.setRelativeData('.number_flight_time','N');
                                this.setRelativeData('.minutes','-');
                                this.setRelativeData('.seconds','-');
                                this.setRelativeData('.tenths','-');
                            };
                            """, row_count='^.selected_row_count',
                            minutes='^.selected_minutes', seconds='^.selected_seconds',tenths='^.selected_tenths')


    def flight_time_view(self,center):
        center.inlineTableHandler(table='f3kp.flight_time',
                        viewResource='ViewFromPilotMobile',
                        datapath='flight_time', 
                        nodeId='flight_time', 
                        condition='@combination_id.pilot_id=:pid AND @combination_id.@competition_task_id.state_code=:state',
                        condition_pid='^entry.current_pilot_id',
                        condition_state='S',
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
                        )

    def show_edit_time(self,cp):
        cp.data('.minutes','-')
        cp.data('.seconds','-')
        cp.data('.tenths','-')
        cp.data('.selected_','selected_')
        cp.data('.number_flight_time','N')


        time_table=cp.table(margin=0,margin_top='0',_class='^.selected_') # il margin imposta un equo spazio a sinistra e a destra del bo
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
        time_table=cp.table(margin='auto',_class='btn_digit',border_spacing=0,border_collapse='collapse')
        tbody=time_table.tbody(align='center')
        row=tbody.tr()
        cel=row.td(padding='0px')
        cel.button('7',action="genro.publish('insertDigit',{digit:7,selected_:'.selected_'})")
        cel=row.td(padding='0px')
        cel.button('8',action="genro.publish('insertDigit',{digit:8,selected_:'.selected_'})")
        cel=row.td(padding='0px')
        cel.button('9',action="genro.publish('insertDigit',{digit:9,selected_:'.selected_'})")

        row=tbody.tr()
        cel=row.td(padding='0px')
        cel.button('4',action="genro.publish('insertDigit',{digit:4,selected_:'.selected_'})")
        cel=row.td(padding='0px')
        cel.button('5',action="genro.publish('insertDigit',{digit:5,selected_:'.selected_'})")
        cel=row.td(padding='0px')
        cel.button('6',action="genro.publish('insertDigit',{digit:6,selected_:'.selected_'})")
        
        row=tbody.tr()
        cel=row.td(padding='0px')
        cel.button('1',action="genro.publish('insertDigit',{digit:1,selected_:'.selected_'})")
        cel=row.td(padding='0px')
        cel.button('2',action="genro.publish('insertDigit',{digit:2,selected_:'.selected_'})")
        cel=row.td(padding='0px')
        cel.button('3',action="genro.publish('insertDigit',{digit:3,selected_:'.selected_'})")
    

        row=tbody.tr()
        cel=row.td(padding='0px')
        cel.button('0',action="genro.publish('insertDigit',{digit:0,selected_:'.selected_'})")
        cel=row.td(padding='0px')
        cel.button('-',action="genro.publish('removeDigit',{selected_:'.selected_'})")
        cel=row.td(padding='0px')
        cel.button('+',action="""genro.publish('saveTime',{minutes:'^.minutes',seconds:'^.seconds',tenths:'^.tenths',
                                selected_flight_time_id:'^.selected_flight_time_id'})""")

        cp.dataController("""this.setRelativeData('.minutes','-');
                            this.setRelativeData('.seconds','-');
                            this.setRelativeData('.tenths','-');
                            this.setRelativeData('.selected_','selected_');
                         """,fire='^.clear_display')

        cp.dataRpc('.clear_display',self.addTime,combination_id='=.combination_id_for_entry',subscribe_saveTime=True)
        
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
        font_size_top_bars= '18px'
        bar = pane.slotToolbar('2,pageTitle,*,logoutButton,2',childname='upper',font_size=font_size_top_bars)
        bar.pageTitle.div('^.current_full_name',font_weight='bold')
        bar.logoutButton.button('Logout',action='genro.logout();')

    def entryToolbar(self,pane):
        font_size_top_bars2= '11px'
        font_size_top_bars3= '11px'
        bar2 = pane.slotToolbar('2,combination,*',childname='lower',_position='>upper')
        bar2.combination.div('^.combination_name',font_weight='bold',font_size=font_size_top_bars2)
        bar3 = pane.slotToolbar('*,task,*',childname='lower_lower',_position='>lower')
        bar3.task.div('^.task_description',font_weight='bold',font_size=font_size_top_bars3)

    def message(self,pane,message=None):
        pane.div(message,font_size='25px',text_align='center')

    def pilot_views(self,tc):

        tc.contentPane(title='ROUNDS').plainTableHandler(table='f3kp.combination',datapath='combination',
                                        title='Combinations',
                                        viewResource='View_from_pilot_mobile',
                                        condition="$competition_id=:id",
                                        condition_id='^entry.current_competition_id',
                                        condition_onStart=True,
                                        font_size = '13px',
                                        )
            
        tc.contentPane(title='RANKING').plainTableHandler(table='f3kp.registration',
                                        title='Ranking',
                                        datapath='ranking',
                                        viewResource='ViewFromRanking',
                                        condition="$competition_id=:id",
                                        condition_id='^entry.current_competition_id',
                                        condition_onStart=True,
                                        font_size = '15px',
                                        grid_showLineNumber=True
                                        )