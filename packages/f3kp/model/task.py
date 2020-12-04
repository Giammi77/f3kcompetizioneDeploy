class Table(object):
    def config_db(self, pkg):
        tbl = pkg.table('task', pkey='code', name_long='!![en]Task', 
                        name_plural='!![en]Tasks',caption_field='description',lookup=True)
        self.sysFields(tbl,id=False)
        tbl.column('code' ,size=':3',name_long='!![it]Task',validate_case='u',validate_notnull=True)
        tbl.column('description',name_long='!![en]Description',validate_case='u')
        tbl.column('operative_time', dtype='N', name_long='!![en]Operative Time', name_short='O.T.')
        