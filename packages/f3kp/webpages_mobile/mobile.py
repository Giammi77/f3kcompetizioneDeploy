# -*- coding: utf-8 -*-
from gnr.core.gnrdecorator import public_method

class GnrCustomWebPage(object):
    py_requires = 'th/th:TableHandler'

    def main(self,pane,**kwargs):
        contenitore= pane.div('Ciaoooo',class='selected_contenitore')