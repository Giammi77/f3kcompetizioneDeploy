# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl=pkg.table('managment', pkey='id', name_long='!![en]Managment',caption_field='managment_description')
        self.sysFields(tbl)

        tbl.column('competition_task_id', size='22', group='_',name_long='!![en]Competition Task'
                    ).relation('competition_task.id',
                                relation_name='managment',
                                mode='foreingkey',
                                onDelete='cascade')

        tbl.column('state_code', size='1', name_long='!![en]State').relation('state.code',
                                relation_name='managment', 
                                mode='foreingkey',
                                onDelete='cascade')

        tbl.column('task_group_code', size='1',group='_', name_long='!![en]Group',name_short='Group',
                    ).relation('task_group.code',
                                relation_name='managment',
                                mode='foreingkey',
                                onDelete='cascade')
        tbl.column('operative_time',dtype='N', name_long='!![en]Operative Time')
        tbl.column('preparation_time',dtype='N', name_long='!![en]Preparation Time')
        tbl.column('time_end',dtype='D', name_long='!![en]End Time')
        tbl.column('activated', dtype='B', name_long='!![en]Task activated')
        tbl.aliasColumn('competition_id', '@competition_task_id.competition_id')
        tbl.aliasColumn('task_code', '@competition_task_id.task_code')
        tbl.aliasColumn('competition_task_row_count','@competition_task_id._row_count')
        tbl.formulaColumn('managment_description','''@competition_task_id.@competition_id.name_competition || ' Round '
                                || @competition_task_id._row_count || ' Group ' || @task_group_code.description ''',name_long='!![en]Combination') 

