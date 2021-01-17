#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('code')
        r.fieldcell('description')

    def th_order(self):
        return 'code'

    def th_query(self):
        return dict(column='code', op='contains', val='')



class Form(BaseComponent):

    def th_form(self, form):
        bc=form.center.borderContainer()
        top=bc.contentPane(region='top',height='30px',datapath='.record')
        center=bc.contentPane(region='center')
        
        fb = top.formbuilder(cols=2, border_spacing='4px')
        fb.field('code')
        fb.field('description',width='40em')

        center.inlineTableHandler(relation='@timer_setup',viewResource='View_from_timer')

    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px')

# MI SERVIRA' POI PER ESPORTARE LA PLAYLIST PER IL TIMER IN LOCALE
    # def test_1_download_text(self,pane):
    #     """First test description"""
    #     fb = pane.formbuilder(cols=1,border_spacing='3px')
    #     fb.textbox(value='^.name',lbl='Name')
    #     fb.data('.name',"hello")
    #     fb.button('Download file',action='genro.rpcDownload(rpcmethod,{name:name+".txt"})',
    #                 rpcmethod=self.testDownloadFile,
    #                 name='=.name')