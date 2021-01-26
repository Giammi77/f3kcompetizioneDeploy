# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl=pkg.table('combination', pkey='id', name_long='!![en]Combination', name_plural='!![en]Combinations',
                        caption_field='combination_name')
        self.sysFields(tbl)

        tbl.column('competition_task_id', size='22', group='_',name_long='!![en]Competition Task'
                    ).relation('competition_task.id',
                                relation_name='combination',
                                mode='foreingkey',
                                onDelete='cascade')

        tbl.column('task_group_code', size='1',group='_', name_long='!![en]Group',name_short='Group',
                    ).relation('task_group.code',
                                relation_name='combination',
                                mode='foreingkey',
                                onDelete='cascade')

        tbl.column('pilot_id', size='22',group='_', name_long='!![en]Pilot',
                    ).relation('pilot.id',
                                relation_name='combination',
                                mode='foreingkey',
                                onDelete='cascade')
        tbl.column('weight', dtype='N', name_long='!![en]Pilot weight')
        tbl.column('time_registred', dtype='B', name_long='!![en]Time registred')
        tbl.column('accept_times',dtype='B', name_long='!![en]Allow insert flight time',batch_assign=True)



        # tbl.aliasColumn('competition_task__row_count',"@competition_task_id._row_count") #forse è doppia!!

        # tbl.aliasColumn('competition_task_state_code','@competition_task_id.state_code')
        tbl.formulaColumn('managment_activated',select=dict(table='f3kp.managment',
                                                    columns='$activated',
                                                    where='''$task_group_code=#THIS.task_group_code 
                                                            AND  $competition_task_id=#THIS.competition_task_id
                                                            '''),
                                                    dtype='B', name_long='!![en]Current Task')
        tbl.formulaColumn('combination_name','''@competition_task_id.@competition_id.name_competition || ' Round '
                             || @competition_task_id._row_count || ' Group ' || @task_group_code.description ''',name_long='!![en]Combination') 
 
        tbl.formulaColumn('avg_weight',select=dict(table='f3kp.combination',
                                                    columns='AVG(weight)',
                                                    where='$task_group_code=#THIS.task_group_code AND  $competition_id=#THIS.competition_id'),
                                                    dtype='N', name_long='!![en]Average weight')

        tbl.formulaColumn('flight_1',select=dict(table='f3kp.flight_time',
                                                    columns='$flight_time',
                                                    where='$combination_id=#THIS.id AND $_row_count=1'),
                                                    dtype='N', name_long='!![en]Flight 1')

        tbl.formulaColumn('flight_2',select=dict(table='f3kp.flight_time',
                                                    columns='$flight_time',
                                                    where='$combination_id=#THIS.id AND $_row_count=2'),
                                                    dtype='N', name_long='!![en]Flight 2')

        tbl.formulaColumn('flight_3',select=dict(table='f3kp.flight_time',
                                                    columns='$flight_time',
                                                    where='$combination_id=#THIS.id AND $_row_count=3'),
                                                    dtype='N', name_long='!![en]Flight 3')

        tbl.formulaColumn('flight_4',select=dict(table='f3kp.flight_time',
                                                    columns='$flight_time',
                                                    where='$combination_id=#THIS.id AND $_row_count=4'),
                                                    dtype='N', name_long='!![en]Flight 4')  

        tbl.formulaColumn('flight_5',select=dict(table='f3kp.flight_time',
                                                    columns='$flight_time',
                                                    where='$combination_id=#THIS.id AND $_row_count=5'),
                                                    dtype='N', name_long='!![en]Flight 5')

        tbl.formulaColumn('flight_6',select=dict(table='f3kp.flight_time',
                                                    columns='$flight_time',
                                                    where='$combination_id=#THIS.id AND $_row_count=6'),
                                                    dtype='N', name_long='!![en]Flight 6')

        tbl.formulaColumn('flight_7',select=dict(table='f3kp.flight_time',
                                                    columns='$flight_time',
                                                    where='$combination_id=#THIS.id AND $_row_count=7'),
                                                    dtype='N', name_long='!![en]Flight 7')

        tbl.formulaColumn('time_flew',select=dict(table='f3kp.flight_time',
                                                    columns='SUM($flight_time)',
                                                    where='$combination_id=#THIS.id'),
                                                    dtype='score', name_long='!![en]Time flew')

        tbl.formulaColumn('time_flew_max',select=dict(table='f3kp.combination',
                                                    columns='MAX($time_flew)',
                                                    where='$competition_task_id=#THIS.competition_task_id AND $task_group_code=#THIS.task_group_code'),
                                                    dtype='N', name_long='!![en]Time flew max')

        tbl.formulaColumn('score',"CASE WHEN $time_flew = 0 THEN  0 ELSE $time_flew/$time_flew_max*1000 END",name_long='!![en]Score',dtype='score')

        tbl.formulaColumn('total_score',select=dict(table='f3kp.combination',
                                                    columns='SUM($score)',
                                                    where='$pilot_id=#THIS.pilot_id AND $competition_id=#THIS.competition_id'),
                                                    dtype='score',name_long='!![en]Total Score')

        tbl.aliasColumn('round_number','@competition_task_id._row_count',name_long='!![en]Round Number',name_short='!![en]Rnd.Nr.')
        tbl.aliasColumn('competition_id','@competition_task_id.competition_id',name_long='!![en]Competition')
        tbl.aliasColumn('task_description','@competition_task_id.@task_code.description',name_long='!![en]Task description')
        tbl.aliasColumn('task_operative_time','@competition_task_id.@task_code.operative_time',name_long='!![en]Operative Time')
    
        tbl.aliasColumn('task_group_code_announcement','@task_group_code.announcement')
        # tbl.aliasColumn('file_name','@competition_task_id.@task_code.file_name')
        # tbl.aliasColumn('glider_score_string','@competition_task_id.@task_code.glider_score_string')
        # tbl.aliasColumn('timer_code','@competition_task_id.@task_code.timer_code')

    def upgrade_time_registred(self,id=None,bol=None):
    #     update(record, old_record=None, pkey=None, **kwargs) method of gnr.sql.gnrsqltable.SqlTable instance
    # Update a single record

        record=self.record(id,mode='bag')
        record['time_registred']=bol
        self.update(record)
        