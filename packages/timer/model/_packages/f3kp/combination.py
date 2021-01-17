# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl=pkg.table('combination')
       
        tbl.aliasColumn('announcement_name','@pilot_id.announcement_name',name_long='!![en]Announcement Name')
