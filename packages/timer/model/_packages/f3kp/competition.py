class Table(object):
    def config_db(self,pkg):
        tbl=pkg.table('competition')
        tbl.column('play_list',name_long='!![en]Play List')
        tbl.column('audio_path', name_long='!![en]Audio path')

    
    
