# -*- coding: utf-8 -*-

# sharedobjects.py
# Created by Francesco Porcari on 2012-01-03.
# Copyright (c) 2012 Softwell. All rights reserved.

from gnr.core.gnrdecorator import public_method
from gnr.core.gnrbag import Bag
import threading
import count_down as cd
        
"Test sharedobjects"
class GnrCustomWebPage(object):

    # def main(self,pane,**kwargs):
    #     pane.sharedObject('mydata',shared_id='so_test1',autoLoad=True)
    #     fb=pane.formbuilder(cols=1, datapath='mydata2')
    #     fb.textbox('^.name', lbl='Name')
    #     fb.textbox('^.address', lbl='Address')
    #     fb.numbertextbox('^.age', lbl='Age')

    def main(self,pane,**kwargs):
        pane.data('countDown',None,serverpath='countDown')
        pane.div('CountDown')
        pane.div('^countDown')
        pane.button('press for countDown', action='FIRE rpc')

        pane.dataRpc('result',self.mioCountDown,_fire='^rpc')
        pane.dataController("if (result=='end'){alert('Task Ultimata !!')}",countDown='^countDown',result='^result')
    @public_method
    def mioCountDown(self):
        timeCountDown=[10]
        x = threading.Thread(target=cd.countDown, args=(timeCountDown,))
        x.start()
        while timeCountDown[0]!=0:
            self.pageStore().setItem('countDown',timeCountDown[0])
        x.join()
        return "end"