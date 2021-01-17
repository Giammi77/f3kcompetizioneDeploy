from gnr.web.batch.btcaction import BaseResourceAction
import f3kvoice as voice

caption='Make Voice' #nome del menu del batch
tags='admin' #autorizzazione al batch
description='Make voices for the competition' #nome più completo

class Main(BaseResourceAction):
    batch_prefix = 'AS'
    batch_title = 'Make Voice'
    batch_cancellable=True
    
    def do(self):
        # sn = self.site.storageNode('site:voices')
        # path = sn.internal_path

        audio=self.db.table('timer.audio')

        registration=self.db.table('f3kp.registration')
        task=self.db.table('f3kp.task')
        task_group=self.db.table('f3kp.task_group')

        # competition_task=self.db.table('f3kp.competition_task')
        # combination=self.db.table('f3kp.combination')

        #per ottentere i valori dei parametri richiersti self.batch_parameters
        #per ottenere i record selezionati s=get_selection poi s.data()
        #
        #OTTENGO id delle competition 
 
        selection=self.get_selection(columns='id')
        if not selection:
            return
        #PER OGNI id 
        for e in selection:
            competition_id=e.get('id').strip()
            pilots=registration.query(columns='$pilot_id,$announcement_name',where='$competition_id=:competition_id',competition_id=competition_id).fetch()
            for pilot in pilots:
                #SE ESISTE GIA' UNA VOCE NON LA GENERO
                announcement=pilot['announcement_name']
                announcement_file_name=announcement+'.mp3'
                f=audio.query(columns='file_name',
                where='$file_name= :announcement_file_name',announcement_file_name=announcement_file_name).fetch()
                if f:
                    continue
                new_record=audio.newrecord(
                                            description=announcement,
                                            phonetic=announcement,
                                            file_name=announcement_file_name,
                                            audio_type='PILOT')
                
                audio.insert(new_record)
                self.db.commit()

            tasks=task.query(columns='$announcement,$file_name').fetch()
            for task in tasks:
                #SE ESISTE GIA' UNA VOCE NON LA GENERO
                announcement=task['announcement']
                file_name=task['file_name']
                f=audio.query(columns='file_name',
                where='$file_name= :file_name',file_name=file_name).fetch()
                if f:
                    continue
                new_record=audio.newrecord(
                                            description=announcement,
                                            phonetic=announcement,
                                            file_name=file_name,
                                            audio_type='TASK')
                
                audio.insert(new_record)
                self.db.commit()
            
            task_groups=task_group.query(columns='$announcement').fetch()
            for group in task_groups:
                #SE ESISTE GIA' UNA VOCE NON LA GENERO
                announcement=group['announcement']
                file_name=announcement+'.mp3'
                f=audio.query(columns='file_name',
                where='$file_name= :file_name',file_name=file_name).fetch()
                if f:
                    continue
                new_record=audio.newrecord(
                                            description=announcement,
                                            phonetic=announcement,
                                            file_name=file_name,
                                            audio_type='GROUP')
                
                audio.insert(new_record)
                self.db.commit()


