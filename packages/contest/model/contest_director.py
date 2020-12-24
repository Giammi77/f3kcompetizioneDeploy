# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl=pkg.table('contest_director', pkey='id', name_long='!![en]Contest Director',
                        name_plural='!![en]Contest Directors',caption_field='full_name')
        self.sysFields(tbl)
        tbl.column('first_name', size=':60', name_long='!![en]First Name',validate_case='u')
        tbl.column('last_name', size=':60', name_long='!![en]Last Name',validate_case='u')
        tbl.column('user_id', name_long='User Id').relation('adm.user.id',one_one=True)
        tbl.formulaColumn('full_name', "$last_name || ' ' || LEFT($first_name,1) || '.'"
                            ,name_long='!![en]Full Name') 
    
    def partitionioning_pkeys(self):
        if not self.db.currentEnv.get('contest_director_id'):
            where=None
        else:
            where='$id=:env_contest_director_id'
        return [r['pkey'] for r in self.query(where=where).fetch()]