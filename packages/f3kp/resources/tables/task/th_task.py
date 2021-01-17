#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method
# class LookupView(BaseComponent):

    # def th_struct(self,struct):
    #     r = struct.view().rows()
    #     r.fieldcell('codice',edit=dict(edit=True,validate_case='u',validate_len='5',
    #                 validate_len_error='Massimo 5 caratteri ammessi'),width='6em')
    #     r.fieldcell('descrizione',edit=dict(edit=True,validate_case='u'),width='10em')
    #     r.fieldcell('aliquota',edit=dict(edit=True),width='10em')
class LookupView(BaseComponent):
    
    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('code',text_align='center',edit=dict(edit=True,validate_case='u'))
        r.fieldcell('description',width='50em',edit=dict(edit=True,validate_case='u'))
        r.fieldcell('operative_time',edit=True)
        r.fieldcell('announcement',edit=True)
        r.fieldcell('file_name',edit=True)
        r.fieldcell('timer_code',edit=True)

    def th_order(self):
        return 'code'

    def th_query(self):
        return dict(column='description', op='contains', val='')



class Form(BaseComponent):

    def th_form(self, form):
        pane = form.record
        fb = pane.formbuilder(cols=2, border_spacing='4px')
        fb.field('code' )
        fb.field('description' )
        fb.field('operative_time' )


    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px' )
