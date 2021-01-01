# -*- coding: utf-8 -*-

# drop_uploader.py
# Created by Francesco Porcari on 2010-10-01.
# Copyright (c) 2010 Softwell. All rights reserved.

"""Test drop uploader"""
from __future__ import print_function

from builtins import object
from gnr.core.gnrlist import XlsReader
from gnr.core.gnrbag import Bag, DirectoryResolver
from gnr.core.gnrdecorator import public_method

class GnrCustomWebPage(object):
    py_requires = """gnrcomponents/testhandler:TestHandlerFull,
                   gnrcomponents/drop_uploader"""
    css_requires='public'

          

    def test_01_lettura_dati_file_system(self, pane):
      pane.button('leggi',action='FIRE .leggi')
      pane.div('^.lettura')
      pane.dataRpc('.lettura',self.leggi,_fire='^.leggi')

    @public_method
    def leggi(self):
      lis=[]
      sn = self.site.storageNode('site:testupload','F3K-1m3m30s.txt')

      out_file = open((sn.internal_path),"r")
      for l in out_file:
        lis.append(l)
          
      out_file.close()

      return lis



    def test_99_multifileDlg(self, pane):
        pane.button('test',
        action="genro.dlg.multiUploaderDialog('Upload timer',{uploadPath:uploadPath,onResult:function(res){genro.bp(true)}});",uploadPath='site:testupload')