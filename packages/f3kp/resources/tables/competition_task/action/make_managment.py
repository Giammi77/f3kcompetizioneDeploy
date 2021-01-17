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

        selection=self.get_records()

        tbl_managment=self.db.table('f3kp.managment')

    
        #PER OGNI TASK DEVO CREARE IL MANAGMENT PER OGNI GRUPPO DELLA TASK
        for e in selection:

            competition_id=e.get('competition_id')
            competition_task_id=e.get('id')
            state_code=e.get('state_code')
            number_groups=e.get('number_groups')
            operative_time=e.get('operative_time')
            preparation_time=e.get('preparation_time')
            
            for g in range(number_groups):
                #se esiste già un managment del gruppo non lo genero

                f=tbl_managment.query(
                                            columns='$id,$competition_task_id,$task_group_code',
                                            where='$competition_task_id=:competition_task_id AND $task_group_code=:task_group_code',
                                            competition_task_id= competition_task_id,
                                            task_group_code=str(g+1)).fetch()

                if f:
                    continue
            
                managment=tbl_managment.newrecord(competition_task_id=competition_task_id,
                                        state_code='A',
                                        task_group_code=str(g+1),
                                        operative_time=operative_time,
                                        preparation_time=preparation_time,
                                        )
                
                tbl_managment.insert(managment)
                self.db.commit()

