# encoding: utf-8
from gnr.core.gnrdecorator import metadata
class Table(object):
    def config_db(self, pkg):
        tbl = pkg.table('state', pkey='code', name_long='!![en]State', 
                        name_plural='!![en]States',caption_field='description',lookup=True)
        self.sysFields(tbl,id=False)
        tbl.column('code' ,size='1',name_long='!![en]State')
        tbl.column('description', size=':30',name_long='!![en]Description')

    @metadata(mandatory=True)
    def sysRecord_A(self):
        return self.newrecord(code='A',
                            description='APPROVED')

    @metadata(mandatory=True)
    def sysRecord_E(self):
        return self.newrecord(code='E',
                            description='ENDED')

    @metadata(mandatory=True)
    def sysRecord_P(self):
        return self.newrecord(code='P',
                            description='PAUSED')
    @metadata(mandatory=True)
    def sysRecord_S(self):
        return self.newrecord(code='S',
                            description='STARTED')

    @metadata(mandatory=True)
    def sysRecord_T(self):
        return self.newrecord(code='T',
                            description='TO BE APPROVED')
