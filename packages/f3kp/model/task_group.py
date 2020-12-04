class Table(object):
    def config_db(self, pkg):
        tbl = pkg.table('task_group', pkey='code', name_long='!![en]Task group', 
                        name_plural='!![en]Task groups',caption_field='description',lookup=True)
        self.sysFields(tbl,id=False)
        tbl.column('code' ,size='1',name_long='!![en]Group',validate_case='u',validate_notnull=True)
        tbl.column('description',name_long='!![en]Description',validate_case='u')
      
        