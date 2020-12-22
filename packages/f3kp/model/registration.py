# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl=pkg.table('registration', pkey='id', name_long='!![en]Registration', name_plural='!![en]Registrations',
                    caption_field='registered_pilot')
        self.sysFields(tbl,counter='competition_id')

        tbl.column('competition_id', size='22', group='_',name_long='!![en]Competition'
                    ).relation('competition.id',
                                relation_name='registration',
                                mode='foreingkey',
                                onDelete='cascade')

        tbl.column('weight', dtype='N', name_long='!![en]Weight')
        tbl.column('pilot_id', size='22',group='_', name_long='!![en]Pilot',
                    ).relation('pilot.id',
                                relation_name='registration',
                                mode='foreingkey',
                                onDelete='cascade')

        tbl.aliasColumn('full_name','@pilot_id.full_name',name_long='!![en]Full Name')

        # tbl.aliasColumn('total_score','@competition_id.@competition_task.@combination.total_score',name_long='!![en]Total Score')
        tbl.formulaColumn('total_score',select=dict(table='f3kp.combination',
                                            columns='MAX($total_score)',
                                            where='$pilot_id=#THIS.pilot_id AND $competition_id=#THIS.competition_id'),name_long='!![en]Total Score',
                                            dtype='score')

        tbl.formulaColumn('competition_state_code',select=dict(table='f3kp.competition',
                                            columns='$state_code',
                                            where='$id=#THIS.competition_id'))
       
    def defaultValues(self):
        return dict(weight=100)        



