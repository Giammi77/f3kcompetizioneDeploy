# -*- coding: utf-8 -*-

# drop_uploader.py
# Created by Francesco Porcari on 2010-10-01.
# Copyright (c) 2010 Softwell. All rights reserved.

from __future__ import print_function

from builtins import object
from gnr.core.gnrlist import XlsReader
from gnr.core.gnrbag import Bag, DirectoryResolver
from gnr.core.gnrdecorator import public_method
import os



class GnrCustomWebPage(object):

    py_requires = """th/th:TableHandler,
                   gnrcomponents/drop_uploader"""
    css_requires='public'

    def main(self,root,**kwargs):
        bc=root.borderContainer(datapath='files')
        top=bc.contentPane(region='top',height='30%')
        center=bc.contentPane(region='center')
        top.button('Import timer setup files',
                action="""genro.dlg.multiUploaderDialog('Upload timer setup files',
                        {uploadPath:uploadPath,onResult:function(res){genro.bp(true)}});""",
                uploadPath='site:timer_setup_importer')
        right=bc.contentPane(region='right',width='30%')
        sn = self.site.storageNode('site:timer_setup_importer')
        path_dir =sn.internal_path
        # path_file = os.sep.join([path_dir])
        resolver= DirectoryResolver(path_dir)
        top.data('.files.timer_setup_importer',resolver())
        top.tree(storepath='.files.timer_setup_importer',hideValues=False,autoCollapse=True,
                    checkChildren=True,checkedPaths='.checked',checkedPaths_joiner='\n',
                    checked_abs_path='.checked_abspath:\n',)
                    #   labelAttribute='nodecaption')
        center.button('Import file in Database',action='FIRE .leggi')
        center.div('^.lettura')
        center.dataRpc('.lettura',self.leggi,_fire='^.leggi',files='=.checked_abspath')
        

    @public_method
    def leggi(self,files):
        
        if not files:
            return
        timer=self.db.table('timer.timer')
        timer_setup=self.db.table('timer.timer_setup')

        l_files=files.rsplit()
        content=''
        # sn = self.site.storageNode('site:testupload','F3K-1m3m30s.txt')
        # out_file = open((sn.internal_path),"r")

        for file in l_files:
            out_file = open(file,"r")
            lines=out_file.readlines()
            code=lines.pop(0).replace('\n','')
            if timer_setup.query(where='$timer_code=:code',code=code).fetch():
                break
            timer_record=timer.query(where='$code=:code',code=code).fetch()
            
            if timer_record[0]['code'].replace(' ','')==code:
                try:
                    for l in lines:
                            l=l.replace('\n','')
                            timer_time,display_time,timer_state_code,announcement,announcement_file_name,beep_frequency,beep_duaration,on_new_round=l.split('|')
                            new_record=timer_setup.newrecord(
                                                            timer_code=code,
                                                            timer_time=timer_time,
                                                            display_time=display_time,
                                                            timer_state_code=timer_state_code,
                                                            announcement=announcement,
                                                            announcement_file_name=announcement_file_name.replace('.wav','.mp3'),
                                                            beep_frequency=beep_frequency,
                                                            beep_duaration=beep_duaration,
                                                            on_new_round=on_new_round)
                            timer_setup.insert(new_record)
                            self.db.commit()
                except:
                    return 'corrupted file'
                out_file.close()
        
        return 'Timer setup imported.'