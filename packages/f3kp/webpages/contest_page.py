# -*- coding: utf-8 -*-
from gnr.core.gnrdecorator import public_method


class GnrCustomWebPage(object):
    py_requires = 'th/th:TableHandler'
    css_requires='f3k_mobile'

    def main(self,pane,**kwargs):
        pane.div('hello !!!')