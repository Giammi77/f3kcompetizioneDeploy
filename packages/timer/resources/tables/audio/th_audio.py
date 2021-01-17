#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('description')
        r.fieldcell('phonetic')
        r.fieldcell('file_name')
        r.fieldcell('audio_type')

    def th_order(self):
        return 'description'

    def th_query(self):
        return dict(column='description', op='contains', val='')



class Form(BaseComponent):

    def th_form(self, form):
        pane = form.record
        fb = pane.formbuilder(cols=2, border_spacing='4px')
        fb.field('description')
        fb.field('phonetic')
        fb.field('file_name')
        fb.field('audio_type')


    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px')
