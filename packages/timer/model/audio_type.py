# encoding: utf-8
from gnr.core.gnrdecorator import metadata
class Table(object):
    def config_db(self, pkg):
        tbl = pkg.table('audio_type', pkey='code', name_long='!![en]Audio Type', 
                        name_plural='!![en]Audio Types',caption_field='description',lookup=True)
        self.sysFields(tbl,id=False)
        tbl.column('code' ,size='15',name_long='!![en]Type')
        tbl.column('description', size=':100',name_long='!![en]Description')

    @metadata(mandatory=True)
    def sysRecord_TASK(self):
        return self.newrecord(code='TASK',
                            description='TASK')

    @metadata(mandatory=True)
    def sysRecord_PILOT(self):
        return self.newrecord(code='PILOT',
                            description='PILOT')

    @metadata(mandatory=True)
    def sysRecord_GROUP(self):
        return self.newrecord(code='GROUP',
                            description='GROUP')
    @metadata(mandatory=True)
    def sysRecord_TIMER(self):
        return self.newrecord(code='TIMER SETUP',
                            description='TIMER SETUP')
    @metadata(mandatory=True)
    def sysRecord_ROUND(self):
        return self.newrecord(code='ROUND',
                            description='ROUND')
