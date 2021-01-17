from gnr.web.batch.btcaction import BaseResourceAction
import f3kvoice as voice

caption='Make Voice' #nome del menu del batch
tags='admin' #autorizzazione al batch
description='Make voices for the announcement' #nome più completo

class Main(BaseResourceAction):
    batch_prefix = 'AS'
    batch_title = 'Make Voice'
    batch_cancellable=True
    
    def do(self):
        # sn = self.site.storageNode('site:voices')
        # path = sn.internal_path
        audio=self.db.table('timer.audio')

        #per ottentere i valori dei parametri richiersti self.batch_parameters
        #per ottenere i record selezionati s=get_selection poi s.data()
        #
        #OTTENGO LE TIMER SETUP SELEZIONATE GENERARE LE VOCI
        selection=self.get_selection(columns='announcement,announcement_file_name')
        
        #PER OGNI TASK TENGO DA PARTE I DATI DELLA TASK IN CASO DI NECESSITA'
        for e in selection:
            announcement=e.get('announcement').strip()
            announcement_file_name=e.get('announcement_file_name').strip()
            #SE CI SONO I DATI 
            if announcement  and announcement_file_name :
                #SE ESISTE GIA' UNA VOCE NON LA GENERO 
                f=audio.query(columns='file_name',
                where='$file_name= :announcement_file_name',announcement_file_name=announcement_file_name).fetch()
                if f:
                    continue
                new_record=audio.newrecord(
                                            description=announcement,
                                            phonetic=announcement,
                                            file_name=announcement_file_name,
                                            audio_type='TIMER SETUP')
                
                audio.insert(new_record)
                self.db.commit()
       
    







