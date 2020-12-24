#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('first_name')
        r.fieldcell('last_name')
        r.fieldcell('user_id')

    def th_order(self):
        return 'first_name'

    def th_query(self):
        return dict(column='full_name', op='contains', val='')



class Form(BaseComponent):

    def th_form(self, form):
        pane = form.record
        fb = pane.formbuilder(cols=2, border_spacing='4px')
        fb.field('first_name' )
        fb.field('last_name' )
        fb.field('user_id' )


    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px' )
