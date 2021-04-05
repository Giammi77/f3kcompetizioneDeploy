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
        return 'date:d'

    def th_query(self):
        return dict(column='name', op='contains', val='')

    def th_options(self):
        return dict(virtualStore=True)

    def th_top_toolbar(self,top):
        state=top.slotToolbar('1,sections@state_code,*',childname='state')


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
        state_code=self.db.table('f3kp.competition').record(competition_id,mode='bag')
        if not state_code['state_code']=='A':
            return

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
        self.db.table('f3kp.competition').notifyDbUpdate(record['competition_id'])
        self.db.commit()
        sleep(3)

class ViewMyCompetition(View):
    def th_struct(self,struct):
        r = struct.view().rows()
        # r.fieldcell('name_competition')
        r.fieldcell('name',edit=False)
        r.fieldcell('venue',edit=False)
        r.fieldcell('date',edit=False)
        r.fieldcell('state_code',edit=False)
    

class ViewFromPilotMobile(View):
    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('name',width='10em')
        r.fieldcell('venue',width='10em')
        r.fieldcell('date',width='5em')
        r.fieldcell('state_code',width='5em')
    def th_top_toolbar(self,top):
        state=top.slotToolbar('sections@state_code,*',childname='state')

class ViewFromRegisteringMobile(ViewFromPilot):
    def th_struct(self,struct):
        r = struct.view().rows()
        # r.fieldcell('name_competition')
        r.fieldcell('name',width='10em')
        r.fieldcell('venue',width='10em')
        r.fieldcell('date',width='5em')
        r.fieldcell('state_code',width='5em')
        r.cell('!![en]Action',calculated=True,format_buttonclass='gear iconbox',
                    format_isbutton=True,
                    format_onclick="""var row = this.widget.rowByIndex($1.rowIndex);
                                    var pilot_id = this.getRelativeData('current_pilot_id');
                                      PUBLISH do_action = {competition_id:row._pkey,pilot_id:pilot_id};""",
                    width='5em')

class Form(BaseComponent):
    #FORM FROM CONTEST DIRECTOR
    def th_form(self, form):
        bc=form.center.borderContainer()
        top=bc.contentPane(region='top',height='15%',datapath='.record')
        center_tb=bc.tabContainer(region='center')
        fb = top.formbuilder(margin_left='20px',margin_right='30px'
                            ,cols=4,cols_width='auto',fld_width='90%')
        fb.field('name')
        fb.field('venue')
        fb.field('date')
        fb.field('state_code')
        fb.field('short_note',colspan=3)
        fb.field('preparation_time') #,validate_notnull=True lo fa solo in questa form o in quelle ereditate?
        
        self.registration(center_tb)
        self.competition_task(center_tb)
        self.combination(center_tb)
        self.ranking(center_tb)
        self.managment(center_tb)
        self.competition_informations(center_tb)

    def registration(self,tc):
        tc.contentPane(title='!![en]Registration Pilot').inlineTableHandler(relation='@registration',
                        viewResource='ViewRegistrationFromCompetition', liveUpdate=True,    #usiamo il liveUpdate per aggiornare automaticamente le competizioni una volta iscritti
                        picker='pilot_id') 

    def competition_task(self,tc):
        tc.contentPane(title='!![en]Task').inlineTableHandler(relation='@competition_task',
                        viewResource='Viewcompetition_taskFromCompetition',
                        picker='task_code',picker_field='task_code') 

    def combination(self,tc):
        tc.contentPane(title='!![en]Combination').dialogTableHandler(table='f3kp.combination',
                                            viewResource='View_from_contest_director',
                                            formResource='FormCombination',
                                            datapath='combination',
                                            condition='$competition_id = :competition_id',
                                            condition_competition_id='^#FORM.pkey',
                                            condition_onStart=True,title="!![en]combination",
                                            liveUpdate=True)
        
    def ranking(self,tc):
        tc.contentPane(title='!![en]Ranking').plainTableHandler(table='f3kp.registration',viewResource='ViewFromRanking',
                                            datapath='ranking',condition_onStart=True,title="!![en]Ranking",
                                            grid_showLineNumber=True,
                                            condition='$competition_id = :competition_id',
                                            condition_competition_id='^#FORM.pkey',
                                            liveUpdate=True)
    # def th_top_custom(self,top):
    #      bar=top.bar.replaceSlots('#','save') 
    def managment(self,tc):
        tc.contentPane(title='!![en]Managment').inlineTableHandler(table='f3kp.managment',viewResource='View',
                                            datapath='managment',
                                            condition='$competition_id = :competition_id',
                                            condition_competition_id='^#FORM.pkey',
                                            condition_onStart=True,title="!![en]Managment",
                                            liveUpdate=True)
                                            # grid_showLineNumber=True)

    def competition_informations(self,tc):
        tc.contentPane(title='!![en]Competition Informations').ckeditor(value='^.competition_informations')


    def th_options(self):
        return dict(dialog_height='600px', dialog_width='600px',delrow=False,addrow=False)

class Form_from_pilot(Form):
    #FORM FOR DESKTOP 
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
        self.competition_task(center_tb)

    def competition_task(self,tc):
        tc.contentPane(title='!![en]Task').plainTableHandler(relation='@competition_task',
                        viewResource='Viewcompetition_taskFromCompetition')

    def combination(self,tc):
        tc.contentPane(title='!![en]Combination').plainTableHandler(table='f3kp.combination',
                                            formResource='FormCombination',
                                            datapath='combination',
                                            condition='$competition_id = :competition_id',
                                            condition_competition_id='^#FORM.pkey',
                                            viewResource='View_from_contest_director',
                                            condition_onStart=True,title="!![en]combination")

    def ranking(self,tc):
        tc.contentPane(title='!![en]Ranking').plainTableHandler(table='f3kp.registration',viewResource='ViewFromRanking',
                                            datapath='ranking',
                                            condition='$competition_id = :competition_id',
                                            condition_competition_id='^#FORM.pkey',
                                            condition_onStart=True,title="!![en]Ranking",
                                            grid_showLineNumber=True)

    def th_options(self):
        return dict(dialog_height='800px', dialog_width='800px')

class Form_from_pilot_mobile(Form_from_pilot):
    def th_form(self, form):
        bc=form.center.borderContainer()
        top=bc.contentPane(region='top',height='20%',datapath='.record')
        center_tb=bc.tabContainer(region='center')
        fb = top.formbuilder(margin_left='0px',margin_right='10px'
                            ,cols=2,cols_width='auto',fld_width='100%')
        fb.field('date',readOnly=True)
        fb.field('state_code',colspan=2,readOnly=True)

        fb.field('name',readOnly=True,width='5em')
        fb.field('venue',readOnly=True)
        
        fb.field('short_note',colspan=2,readOnly=True)
        self.combination(center_tb)
        self.ranking(center_tb)
        self.competition_task(center_tb)
    def th_top_custom(self,top):
        bar=top.bar.replaceSlots('#','') 