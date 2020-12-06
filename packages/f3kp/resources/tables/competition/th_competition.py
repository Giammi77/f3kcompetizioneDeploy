#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method
from time import sleep
class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        # r.fieldcell('name_competition')
        r.fieldcell('name')
        r.fieldcell('venue')
        r.fieldcell('date')
        r.fieldcell('state_code')


    def th_order(self):
        return 'date'

    def th_query(self):
        return dict(column='name', op='contains', val='')

    def th_options(self):
        return dict(virtualStore=True)



class ViewFromPilot(View):

    def th_struct(self,struct):
        r = struct.view().rows()
        # r.fieldcell('name_competition')
        r.fieldcell('name')
        r.fieldcell('venue')
        r.fieldcell('date')
        r.fieldcell('state_code')
        r.cell('!![en]Action',calculated=True,format_buttonclass='gear iconbox',
                    format_isbutton=True,
                    format_onclick="""var row = this.widget.rowByIndex($1.rowIndex);
                                    var pilot_id = this.getRelativeData('main.current_pilot_id');
                                      PUBLISH do_action = {competition_id:row._pkey,pilot_id:pilot_id};""")
                    #                   ,
                    # cellClassCB="""var row = cell.grid.rowByIndex(inRowIndex);
                    #                 if(row._state_description != "APPROVED"){
                    #                     return 'hidden';
                    #                 }""")
        
        # r.fieldcell('check_pilot_signed')
        # r.cell('pycolumn',calculated=True)
        # r.cell('azione',calculated=True,format_buttonclass='gear iconbox',
        #             format_isbutton=True,
        #             format_onclick="""var row = this.widget.rowByIndex($1.rowIndex);
        #                               PUBLISH esegui_azione = {prodotto_id:row._pkey};""",
        #             cellClassCB="""var row = cell.grid.rowByIndex(inRowIndex);
        #                             if(row.codice=='C1'){
        #                                 return 'hidden';
        #                             }""")
        # format_onclick="""var row = this.widget.rowByIndex($1.rowIndex); row è un dizionario 
        #                                                                   con i dati del record
        #                   console.log(row);""",



    def th_view(self,view):
        view.dataRpc('dummy',self.signIn,subscribe_do_action=True,_lockScreen=dict(message='Registering pilot'))
        

    @public_method
    def signIn(self,competition_id=None,pilot_id=None):
        f_registration=self.db.table('f3kp.registration').query(column='$competition_id,$pilot_id',
                            where ='$competition_id=:pr_competition_id AND $pilot_id=:pr_pilot_id',
                            pr_competition_id=competition_id,
                            pr_pilot_id=pilot_id).fetch()

        if len(f_registration)==1:
            #existing registration
            return 
        tbl_registration=self.db.table('f3kp.registration')
        record= tbl_registration.newrecord() 
        record['competition_id'] = competition_id
        record['pilot_id'] = pilot_id
        record['weight'] = 100
        tbl_registration.insert(record)
        self.db.commit()
        sleep(1)

class ViewMyCompetition(View):
    def th_struct(self,struct):
        r = struct.view().rows()
        # r.fieldcell('name_competition')
        r.fieldcell('name',edit=False)
        r.fieldcell('venue',edit=False)
        r.fieldcell('date',edit=False)
        r.fieldcell('state_code',edit=False)

class Form(BaseComponent):

    def th_form(self, form):
        bc=form.center.borderContainer()
        top=bc.contentPane(region='top',height='15%',datapath='.record')
        center_tb=bc.tabContainer(region='center')
        fb = top.formbuilder(cols=3, border_spacing='4px')
        fb.field('name')
        fb.field('venue')
        fb.field('date')
        fb.field('state_code')
 

        self.registration(center_tb)
        self.competition_task(center_tb)
        self.combination(center_tb)
        self.ranking(center_tb)


    def registration(self,tc):
        tc.contentPane(title='!![en]Registration Pilot').inlineTableHandler(relation='@registration',
                        viewResource='ViewRegistrationFromCompetition',
                        picker='pilot_id') 

    def competition_task(self,tc):

        tc.contentPane(title='!![en]Task').inlineTableHandler(relation='@competition_task',
                        viewResource='Viewcompetition_taskFromCompetition',
                        picker='task_code',picker_field='task_code') 

    def combination(self,tc):
        tc.contentPane(title='!![en]Combination').dialogTableHandler(table='f3kp.combination',
                                            formResource='FormCombination',
                                            datapath='combination',
                                            condition='$competition_id = :competition_id',
                                            condition_competition_id='^#FORM.pkey',
                                            viewResource='View_from_contest_director',
                                            condition_onStart=True,title="!![en]combination")
        
    def ranking(self,tc):
        tc.contentPane(title='!![en]Ranking').plainTableHandler(table='f3kp.registration',viewResource='ViewFromRanking',
                                            datapath='ranking',condition_onStart=True,title="!![en]Ranking",
                                            grid_showLineNumber=True)

    def th_options(self):
        return dict(dialog_height='600px', dialog_width='600px')

class Form_from_pilot(Form):
    def th_form(self, form):
        bc=form.center.borderContainer()
        top=bc.contentPane(region='top',height='15%',datapath='.record')
        center_tb=bc.tabContainer(region='center')
        fb = top.formbuilder(cols=3, border_spacing='4px')
        fb.field('name',readOnly=True)
        fb.field('venue',readOnly=True)
        fb.field('date',readOnly=True)
        fb.field('state_code',readOnly=True)
 

        # self.registration(center_tb)
        # self.competition_task(center_tb)
        self.combination(center_tb)
        self.ranking(center_tb)

    def combination(self,tc):
        tc.contentPane(title='!![en]Combination').plainTableHandler(table='f3kp.combination',
                                            formResource='FormCombination',
                                            datapath='combination',
                                            condition='$competition_id = :competition_id',
                                            condition_competition_id='^#FORM.pkey',
                                            viewResource='View_from_contest_director',
                                            condition_onStart=True,title="!![en]combination")












    def th_top_custom(self,top):
         bar=top.bar.replaceSlots('#','') 



    def th_options(self):
        return dict(dialog_height='800px', dialog_width='800px')