# -*- coding: utf-8 -*-

from gnr.web.batch.btcaction import BaseResourceAction
import random as rnd 

caption='Make Managment' #nome del menu del batch
tags='CDI,admin' #autorizzazione al batch
description='Make list of contest managment' #nome più completo

class Main(BaseResourceAction):
    batch_prefix = 'AS'
    batch_title = 'Contest Managment'
    batch_cancellable=False

    def do(self):
        #per ottentere i valori dei parametri richiersti self.batch_parameters
        #per ottenere i record selezionati s=get_selection poi s.data()
        #
        #OTTENGO LE TASK SELEZIONATE GENERARE LE MATRICI

        selection=self.get_selection()
    
        
        tbl_managment=self.db.table('f3kp.managment')

    
        #PER OGNI TASK DEVO CREARE IL MANAGMENT PER OGNI GRUPPO DELLA TASK
        for e in selection:

            competition_id=e.get('competition_id')
            competition_task_id=e.get('id')
            task_code=e.get('task_code')
            state_code=e.get('state_code')
            number_groups=e.get('number_groups')
            
            
            tbl_task=self.db.table('f3kp.task')
            tbl_competition=self.db.table('f3kp.competition')
            
            for g in range(number_groups):
                #se esiste già un managment del gruppo non lo genero

                f=tbl_managment.query(
                                            columns='$id,$competition_task_id,$task_group_code',
                                            where='$competition_task_id=:competition_task_id AND $task_group_code=:task_group_code',
                                            competition_task_id= competition_task_id,
                                            task_group_code=str(g+1)).fetch()

                if f:
                    continue
                operative_time=tbl_task.query(columns='$operative_time',where='$code=:task_code',task_code=task_code).fetch()[0]['operative_time']
                preparation_time=tbl_competition.query(columns='$preparation_time',where='$id=:competition_id',competition_id=competition_id).fetch()[0]['preparation_time']
                
                managment=tbl_managment.newrecord(competition_task_id=competition_task_id,
                                        state_code='A',
                                        task_group_code=str(g+1),
                                        operative_time=operative_time,
                                        preparation_time=preparation_time,
                                        
                                        )
                
                tbl_managment.insert(managment)
                self.db.commit()

