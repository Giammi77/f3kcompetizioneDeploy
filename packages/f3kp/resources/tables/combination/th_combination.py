#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        # r.fieldcell('competition_task_id')
        r.fieldcell('round_number',width='4em',text_align='center')
        r.fieldcell('task_group_code',width='4em',text_align='center')
        r.fieldcell('task_description',width='30em')
        r.fieldcell('pilot_id',width='10em')
        r.fieldcell('weight')
        r.fieldcell('avg_weight')
        r.fieldcell('time_registred')
        
    def th_hiddencolumns(self):
        return "$time_flew_max,$task_group_code"

    def th_order(self):
        return 'round_number,task_group_code'

    def th_query(self):
        return dict(column='combination_name', op='contains', val='')

    def th_top_toolbar(self,top):
        round=top.slotToolbar('1,lbl,2,sections@competition_task_id,*,allow_time',childname='round',_position='>bar')
        round.lbl.div('ROUND')

        group=top.slotToolbar('1,lbl,2,sections@task_group_code,*',childname='group',_position='>round')
        group.lbl.div('GROUP')


    def th_options(self):
        return dict(virtualStore=False)

class View_from_pilot(View):

    def th_struct(self,struct):
        r = struct.view().rows()
        # r.fieldcell('competition_task_id')
        r.fieldcell('round_number',width='4em',text_align='center')
        r.fieldcell('task_group_code',width='4em',text_align='center')
        r.fieldcell('task_description',width='15em')
        r.fieldcell('competition_task_state_code')
        r.fieldcell('pilot_id',width='8em')
        r.fieldcell('flight_1',width='4em')
        r.fieldcell('flight_2',width='4em')
        r.fieldcell('flight_3',width='4em')
        r.fieldcell('flight_4',width='4em')
        r.fieldcell('flight_5',width='4em')
        r.fieldcell('time_flew',width='4em')
        r.fieldcell('score',width='5em')
        r.fieldcell('total_score',width='5em')
        # r.cell('score',calculated=True,
        #   _customGetter="function(row){return parseFloat(row.time_flew/row.time_flew_max*1000).toFixed(2);}",
        #   name='Score',text_align='right')    
 
    def th_order(self):
        return 'round_number,task_group_code,score:d'

class View_from_contest_director(View_from_pilot):
    pass

class View_from_pilot_mobile(View_from_pilot):
    def th_struct(self,struct):
        r = struct.view().rows()
        # r.fieldcell('competition_task_id')
        # r.fieldcell('round_number',width='4em',text_align='center')
        # r.fieldcell('task_group_code',width='4em',text_align='center')
        r.fieldcell('task_description',width='20em')
        r.fieldcell('pilot_id',width='6em')
        r.fieldcell('flight_1',width='3em')
        r.fieldcell('flight_2',width='3em')
        r.fieldcell('flight_3',width='3em')
        r.fieldcell('flight_4',width='3em')
        r.fieldcell('flight_5',width='3em')
        r.fieldcell('time_flew',width='4em')
        r.fieldcell('score',width='4em')
        # r.fieldcell('total_score',width='4em')

class Form(BaseComponent):

    def th_form(self, form):
        pane = form.record
        fb = pane.formbuilder(cols=2, border_spacing='4px')
        fb.field('competition_task_id' )
        fb.field('task_group_code' )
        fb.field('pilot_id' )
        fb.field('weight' )
        fb.field('time_registred' )
       


    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px' )

class FormCombination(Form):
    # py_requires = 'foundation/dialogs'
    def th_form(self, form):
        bc=form.center.borderContainer()
        top=bc.contentPane(region='top',height='15%',width='100%',datapath='.record')
        center_tb=bc.tabContainer(region='center')
        fb=top.div(margin_left='40px',margin_right='70px').formbuilder(cols=4, border_spacing='3px',colswidth='auto',
                                            fld_width='100%')

        fb.field('pilot_id',readOnly=True)
        fb.div()
        fb.div()
        fb.field('time_registred' )

        fb.field('task_description',colspan=2,readOnly=True)
        fb.div()
    
        # fb.field('task_operative_time',readOnly=True)

        self.tempi(center_tb)


    def tempi(self,pane):
        # pane.contentPane(title='Tempi').inlineTableHandler(
        #                                 table='f3kp.flight_time',
        #                                 viewResource='ViewFromCombination',
        #                                 condition='$combination_id=:combination_id',
        #                                 condition_combination_id='^#FORM.pkey')
        pane.contentPane(title='Tempi').inlineTableHandler(
                                        relation='@flight_time',
                                        viewResource='ViewFromCombination',
                                        
                                        )
