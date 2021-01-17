# encoding: utf-8
from gnr.core.gnrdecorator import metadata
class Table(object):
    def config_db(self, pkg):
        tbl = pkg.table('timer_state', pkey='code', name_long='!![en]Timer State', 
                        name_plural='!![en]Timer States',caption_field='description',lookup=True)
        self.sysFields(tbl,id=False)
        tbl.column('code' ,size='2',name_long='!![en]Timer State')
        tbl.column('description', size=':100',name_long='!![en]Description')


    @metadata(mandatory=True)
    def sysRecord_WT(self):
        return self.newrecord(code='WT',
                            description='WORKING TIME')


    @metadata(mandatory=True)
    def sysRecord_PT(self):
        return self.newrecord(code='PT',
                            description='PREPARATION TIME')


    @metadata(mandatory=True)
    def sysRecord_LT(self):
        return self.newrecord(code='LT',
                            description='LANDING TIME')
