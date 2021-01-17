# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl=pkg.table('pilot')
        tbl.formulaColumn('announcement_name', "$last_name || ' ' || $first_name",name_long='!![en]Announcement Name') 
        

