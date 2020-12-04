# encoding: utf-8
class Table(object):
    def config_db(self, pkg):
        tbl = pkg.table('state', pkey='code', name_long='!![en]State', 
                        name_plural='!![en]States',caption_field='description',lookup=True)
        self.sysFields(tbl,id=False)
        tbl.column('code' ,size='1',name_long='!![en]State')
        tbl.column('description', size=':30',name_long='!![en]Description')
