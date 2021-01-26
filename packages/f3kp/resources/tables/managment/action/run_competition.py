# -*- coding: utf-8 -*-

from gnr.web.batch.btcaction import BaseResourceAction
import random as rnd 
from time import time,sleep

caption='Run Competition' #nome del menu del batch
tags='CDI,admin' #autorizzazione al batch
description='Run Competition' #nome più completo

class Main(BaseResourceAction):
    batch_prefix = 'AS'
    batch_title = 'Run Competition'
    batch_cancellable=True

    def do(self):
        #per ottentere i valori dei parametri richiersti self.batch_parameters
        #per ottenere i record selezionati s=get_selection poi s.data()


        selection=self.get_selection(columns="""$id,
                                        $operative_time,
                                        $preparation_time,
                                        $competition_id,
                                        $competition_task_row_count,
                                        $task_group_code""")
        selection.sort('competition_task_row_count,task_group_code')
        tbl_managment=self.db.table('f3kp.managment')
        
        for e in selection:

            managment_id=e.get('id')
            operative_time=e.get('operative_time')
            preparation_time=e.get('preparation_time')
            competition_id=e.get('competition_id')

            tbl_managment=self.db.table('f3kp.managment')
            task_time=operative_time+preparation_time
            py_time_end=time()+int(task_time)
            time_end=py_time_end*1000
        
            
            records_managment=tbl_managment.query(columns='$id,$activated',
                                            where='$competition_id=:competition_id',
                                            competition_id=competition_id
                                            ).fetch()
        
            for r in records_managment:
                
                mangment_id=r['id']
                with self.db.table('f3kp.managment').recordToUpdate(mangment_id) as rec:
                    rec['activated'] = False
                    # rec['time_end']= 0
                self.db.commit()

            with self.db.table('f3kp.managment').recordToUpdate(managment_id) as rec:
                rec['time_end'] = time_end
                rec['activated'] = True
            self.db.commit()
            t=int(task_time)
            sleep(t)
        records_managment=tbl_managment.query(columns='$id,$activated',
                                where='$competition_id=:competition_id',
                                competition_id=competition_id
                                ).fetch()
        
        for r in records_managment:
            
            mangment_id=r['id']
            with self.db.table('f3kp.managment').recordToUpdate(mangment_id) as rec:
                rec['activated'] = False
                # rec['time_end']= 0
            self.db.commit()


