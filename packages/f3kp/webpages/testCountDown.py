# -*- coding: utf-8 -*-

# sharedobjects.py
# Created by Francesco Porcari on 2012-01-03.
# Copyright (c) 2012 Softwell. All rights reserved.

from gnr.core.gnrdecorator import public_method
from gnr.core.gnrbag import Bag
#from gnr.xtnd.gnrpandas import PandasSharedObject


        
"Test sharedobjects"
class GnrCustomWebPage(object):

    def main(self,pane,**kwargs):
        pane.sharedObject('mydata',shared_id='so_test1')
        fb=pane.formbuilder(cols=1, datapath='mydata2')
        fb.textbox('^.name', lbl='Name')
        fb.textbox('^.address', lbl='Address')
        fb.numbertextbox('^.age', lbl='Age')