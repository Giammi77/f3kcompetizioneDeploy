class Table(object):
    def config_db(self,pkg):
        tbl=pkg.table('competition', 
                        partition_contest_director_id='contest_director_id')
        tbl.column('contest_director_id', size='22', name_long='!![en]Contest Director',
                    batch_assign=dict(do_trigger=True),
                    plugToForm=dict(lbl='!![en]Contest Director',readOnly=True)).relation(
                    'contest.contest_director.id',
                    relation_name='competition',
                    mode='foreignkey',onDelete='setnull')
        tbl.aliasColumn('contest_director_full_name','@contest_director_id.full_name',name_long='!![en]Contest Director')
    
    def defaultValues(self):
        default_value=self.defaultValues_()
        default_value.update(dict(contest_director_id=self.db.currentEnv.get('current_contest_director_id')))
        
        return default_value
    
