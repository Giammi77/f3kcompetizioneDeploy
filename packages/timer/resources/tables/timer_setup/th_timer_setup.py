#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('timer_code')
        r.fieldcell('timer_time')
        r.fieldcell('display_time')
        r.fieldcell('timer_state_code')
        r.fieldcell('on_new_round')
        r.fieldcell('announcement')
        r.fieldcell('announcement_file_name')
        # r.fieldcell('beep_frequency')
        # r.fieldcell('beep_duration')
    def th_order(self):
        return 'timer_code'

    def th_query(self):
        return dict(column='timer_code', op='contains', val='')

class View_from_timer(BaseComponent):
    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('timer_code')
        r.fieldcell('timer_time',edit=True)
        r.fieldcell('display_time',edit=True)
        r.fieldcell('timer_state_code',edit=True)
        r.fieldcell('on_new_round',edit=True)
        r.fieldcell('announcement',edit=True)
        r.fieldcell('announcement_file_name',edit=True)
        r.fieldcell('beep_frequency',edit=True)
        r.fieldcell('beep_duaration',edit=True)

    def th_top_custom(self,top):
        bar=top.bar.replaceSlots('#','#,resourceActions,2')
        
    def th_order(self):
        return 'timer_code'

    def th_query(self):
        return dict(column='timer_code', op='contains', val='')


class Form(BaseComponent):

    def th_form(self, form):
        pane = form.record
        fb = pane.formbuilder(cols=2, border_spacing='4px')
        fb.field('timer_code')
        fb.field('timer_time')
        fb.field('display_time')
        fb.field('timer_state_code')
        fb.field('on_new_round')
        fb.field('announcement')
        fb.field('announcement_file_name')


    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px')
