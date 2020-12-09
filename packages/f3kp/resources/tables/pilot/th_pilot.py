#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('full_name',width='10em')
        r.fieldcell('last_name')
        r.fieldcell('first_name')
        
        r.fieldcell('fai_number')
        r.fieldcell('other_regist_number')
        r.fieldcell('fai_id')
        r.fieldcell('pilot_class')
        r.fieldcell('club')
        r.fieldcell('street')
        r.fieldcell('town')
        r.fieldcell('state')
        r.fieldcell('post_code')
        r.fieldcell('country')
        r.fieldcell('email')
        r.fieldcell('private_phone')
        r.fieldcell('work_phone')

    def th_order(self):
        return 'last_name'

    def th_query(self):
        return dict(column='last_name', op='contains', val='')



class Form(BaseComponent):

    def th_form(self, form):
        bc=form.center.borderContainer()
        top=bc.contentPane(region='top', height='200px',datapath='.record')
        tb=bc.tabContainer(region='center')
        
        fb = top.div(margin_left='40px',margin_right='70px').formbuilder(cols=2, border_spacing='4px',colswidth='auto',
                                            fld_width='100%')
        fb.field('last_name')
        fb.field('first_name')
        
        
        fb.field('street')
        fb.field('town')
        
        fb.field('post_code')
        fb.field('state')

        fb.field('country')
        fb.div()

        fb.field('fai_number')
        fb.field('other_regist_number')

        fb.field('fai_id')
        fb.field('pilot_class')

        fb.field('club')
    
        fb.field('email')
        fb.field('private_phone')
        fb.field('work_phone')

        competitions=tb.contentPane(title='!![en]My Competitions')
        
        competitions.dialogTableHandler(table='f3kp.competition',
                                        viewResource='ViewMyCompetition',
                                        condition='@registration.pilot_id=:pr_pilot_id',
                                        condition_pr_pilot_id='^main.current_pilot_id',
                                        condition_onStart=True)

    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px')

class FormPilotPage(Form):
    def th_form(self, form):
        bc=form.center.borderContainer()
        top=bc.contentPane(region='top', height='200px',datapath='.record')
        tb=bc.tabContainer(region='center')
        
        fb = top.div(margin_left='40px',margin_right='70px').formbuilder(cols=2, border_spacing='4px',colswidth='auto',
                                            fld_width='100%')
        fb.field('last_name')
        fb.field('first_name')
        
        
        fb.field('street')
        fb.field('town')
        
        fb.field('post_code')
        fb.field('state')

        fb.field('country')
        fb.div()

        fb.field('fai_number')
        fb.field('other_regist_number')

        fb.field('fai_id')
        fb.field('pilot_class')

        fb.field('club')
    
        fb.field('email')
        fb.field('private_phone')
        fb.field('work_phone')

        competitions=tb.contentPane(title='!![en]My Competitions')
        
        competitions.dialogTableHandler(table='f3kp.competition',
                                        viewResource='ViewMyCompetition',
                                        formResource='Form_from_pilot',
                                        condition='@registration.pilot_id=:pr_pilot_id',
                                        condition_pr_pilot_id='^main.current_pilot_id',
                                        condition_onStart=True,addrow=False,delrow=False,
                                        )
    def th_options(self):
        return dict(showtoolbar=False,autoSave=False)
