# encoding: utf-8
from gnr.core.gnrdecorator import metadata
class Table(object):
    def config_db(self, pkg):
        tbl = pkg.table('timer', pkey='code', name_long='!![en]Timer', 
                        name_plural='!![en]Timers',caption_field='description',lookup=True)
        self.sysFields(tbl,id=False)
        tbl.column('code' ,size='20',name_long='!![en]Timer')
        tbl.column('description', size=':100',name_long='!![en]Description')


    @metadata(mandatory=True)
    def sysRecord_F3K1M3M30S(self):
        return self.newrecord(code='F3K-1m3m30s',
                            description='TIMER FOR F3K TASK 1 MIN PREPARATION TIME, 3 MIN OPERATIVE TIME, 30 SEC LANDING TIME')

    @metadata(mandatory=True)
    def sysRecord_F3K3M15M30S(self):
        return self.newrecord(code='F3K-3m15m30s',
                            description='TIMER FOR F3K TASK 3 MIN PREPARATION TIME, 15 MIN OPERATIVE TIME, 30 SEC LANDING TIME')

    @metadata(mandatory=True)
    def sysRecord_F3K3M7M30S(self):
        return self.newrecord(code='F3K-3m7m30s',
                            description='TIMER FOR F3K TASK 3 MIN PREPARATION TIME, 7 MIN OPERATIVE TIME, 30 SEC LANDING TIME')

    @metadata(mandatory=True)
    def sysRecord_F3K3M3M30S(self):
        return self.newrecord(code='F3K-3m3m30s',
                            description='TIMER FOR F3K TASK 3 MIN PREPARATION TIME, 3 MIN OPERATIVE TIME, 30 SEC LANDING TIME')

    @metadata(mandatory=True)
    def sysRecord_F3K3M10M30S(self):
        return self.newrecord(code='F3K-3m10m30s',
                            description='TIMER FOR F3K TASK 3 MIN PREPARATION TIME, 10 MIN OPERATIVE TIME, 30 SEC LANDING TIME')