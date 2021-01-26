# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl=pkg.table('competition_task', pkey='id', name_long='Competition Task', name_plural='Competition Task',
                        caption_field='competition_task_name')
        self.sysFields(tbl,counter='competition_id')

        tbl.column('competition_id', size='22', group='_',name_long='!![en]Competition'
                    ).relation('competition.id',
                                relation_name='competition_task',
                                mode='foreingkey',
                                onDelete='cascade')

        tbl.column('task_code', size=':3', group='_',name_long='!![en]Task'
                    ).relation('task.code',
                                relation_name='competition_task',
                                mode='foreingkey',
                                onDelete='cascade')
        
        # tbl.column('state_code', size='1', name_long='!![en]State').relation('state.code',
        #                         relation_name='competition_task', 
        #                         mode='foreingkey',
        #                         onDelete='cascade')

        tbl.column('number_groups', dtype='L', name_long='Number Groups', name_short='Nr.Groups')

        tbl.formulaColumn('competition_task_name',"@task_code.description",name_long='!![en]Competition task') 
        # tbl.formulaColumn('competition_task_name',"_row_count",name_long='!![en]Competition task') 
        tbl.aliasColumn('task_code_announcement','@task_code.announcement')
        tbl.aliasColumn('task_code_file_name','@task_code.file_name')
        tbl.aliasColumn('glider_score_string','@task_code.glider_score_string')
        tbl.aliasColumn('timer_code','@task_code.timer_code')
        tbl.aliasColumn('preparation_time','@competition_id.preparation_time')
        tbl.aliasColumn('operative_time','@task_code.operative_time')
        

    def defaultValues(self):
        return dict(state_code='A',number_groups=1) #questo dovrebbe funzionare in caso di batch?