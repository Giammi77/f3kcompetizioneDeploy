#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('_row_count',name='Nr.')
        # r.fieldcell('number_reg',edit=False)
        r.fieldcell('pilot_id',width='15em')
        r.fieldcell('competition_id',width='15em')
        r.fieldcell('weight')

    
    def th_order(self):
        return '_row_count'

    def th_query(self):
        return dict(column='', op='contains', val='')

class ViewRegistrationFromCompetition(View):
    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('_row_count',name='Nr.')
        r.fieldcell('pilot_id',width='15em',edit=dict(edit=True,validate_notnull=True,validate_gridnodup = True))
        r.fieldcell('competition_id',width='15em',edit=True)
        r.fieldcell('weight',edit=dict(edit=True,validate_notnull=True,default_value=100))

class ViewFromRanking(View):
    def th_struct(self,struct):
        r = struct.view().rows()
        # r.fieldcell('_row_count',name='Nr.')
        # r.fieldcell('number_reg',edit=False)
        r.fieldcell('pilot_id',width='15em')
        r.fieldcell('total_score',dtype='score',text_align="right")
        # r.fieldcell('competition_task__row_count')
    def th_order(self):
        return 'score:d'
    def th_options(self):
         return dict(grid_showLineNumber=True)





class Form(BaseComponent):

    def th_form(self, form):
        pane = form.record
        fb = pane.formbuilder(cols=2, border_spacing='4px')
        # fb.field('number_reg',edit=False)
        fb.field('pilot_id' )
        fb.field('competition_id' )
        fb.field('weight')


    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px' )
