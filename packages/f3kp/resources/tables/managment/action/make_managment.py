# -*- coding: utf-8 -*-

from gnr.web.batch.btcaction import BaseResourceAction
import random as rnd 

caption='Make Managment' #nome del menu del batch
tags='admin' #autorizzazione al batch
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
        selection=self.get_selection(columns='competition_id,id,task_code,state_code,number_groups,_row_count')
        
        #PER OGNI TASK TENGO DA PARTE I DATI DELLA TASK IN CASO DI NECESSITA'
        for e in selection:

            competition_id=e.get('competition_id')
            competition_task_id=e.get('id')
            end_task=e.get('state_code')
            number_groups=e.get('number_groups')
           
            
            #SE ESISTE GIA' UNA COMBINAZIONE PER QUESTA TASK NON LA GENERO 
            f=self.db.table('f3kp.combination').query(columns='competition_task_id',
            where='$competition_task_id= :competition_task_id',competition_task_id=competition_task_id).fetch()
            if  f:
                break

            #SE LA TASK E' GIA ULTIMATA LA SALTO SALTO 
            if end_task == 'E':
            
                break
            db=self.db

            #OTTENGO I DATI DEI PILOTI ISCRITTI ALLA GARA
            tbl=db.table('f3kp.registration')
            f=tbl.query(columns='weight,@pilot_id.full_name,_row_count,pilot_id,@pilot_id.full_name',
            where='$competition_id= :competition_id',competition_id=competition_id).fetch()

            diz_piloti,lista_piloti_disponibili,peso_medio,totale_piloti=self.prepara_dati(f)
            piloti_per_gruppo=int(totale_piloti/number_groups)
            limit=0.0001

            # Abbinamenti gruppi task
            while True:
                gruppi_task={}
                lista_piloti_candidati=[p for p in lista_piloti_disponibili]

                for g in range(1,number_groups+1):
                    ultima_task_valida=False
                    if g==number_groups: #se ultimo gruppo non genero i numeri random
                        piloti_gruppo=lista_piloti_candidati
                        pm=self.peso_medio_gruppo(diz_piloti,piloti_gruppo)

                        if (peso_medio*(1-limit)) < pm < (peso_medio*(1+limit)): # se l'ultimo gruppo è conforme hai limiti
                            gruppi_task[g]=piloti_gruppo
                            ultima_task_valida=True
                            break
                        else :
                            break
                    
                    for i in range(100) :
                        piloti_gruppo=self.abbinamenti(lista_piloti_candidati,piloti_per_gruppo)
                        pm=self.peso_medio_gruppo(diz_piloti,piloti_gruppo)

                        if (peso_medio*(1-limit)) < pm < (peso_medio*(1+limit)):
                            gruppi_task[g]=piloti_gruppo
                            break
                        else :
                            for p in piloti_gruppo:
                                lista_piloti_candidati.append(p)
                                
                if ultima_task_valida == True: # se anche l'ultima generazione è andata a buon fine  ho finito gli abbinamenti 
                    break
                else:
                    limit+=0.0001
            #MI ARRIVA IL DIZIONARIO CON gruppi_task VALIDI
            self.crea_abbinamenti(gruppi_task,diz_piloti,competition_task_id)




    # def table_script_parameters_pane(self,pane,extra_parameters=None,
    #                                 record_count=None,**kwargs):
    #     fb=pane.formbuilder()
    #     fb.textbox(value='^.dato_per_batch')

    def crea_abbinamenti(self,gruppi_task,diz_piloti,competition_task_id):
            db=self.db
            #OTTENGO I DATI DEI PILOTI ISCRITTI ALLA GARA
            tbl=db.table('f3kp.combination')
            for gruppo in gruppi_task:
                for pilot_key in gruppi_task[gruppo]:
                    dati_pilota=diz_piloti[pilot_key]
                    newCombination=tbl.newrecord(competition_task_id=competition_task_id,
                                                    task_group_code= gruppo,
                                                    weight=dati_pilota['weight'],
                                                    pilot_id=dati_pilota['pilot_id'])
                    tbl.insert(newCombination)
                    db.commit()

    def prepara_dati(self,dati=None):
        totale_piloti = 0
        totale_peso=0
        lista_piloti_disponibili=[]
        diz_piloti={}
        for e in dati:
            totale_piloti += 1
            totale_peso+=e.get('weight')
            lista_piloti_disponibili.append(e.get('_row_count'))
            diz_piloti[e.get('_row_count')]=e
        totale_piloti += 1
        peso_medio=totale_peso/totale_piloti
        return diz_piloti,lista_piloti_disponibili,float(peso_medio),totale_piloti

    def abbinamenti(self,lista_piloti_candidati,piloti_per_gruppo):
        # if lista_piloti_candidati.__len__()==piloti_per_gruppo:
        #     return lista_piloti_candidati !!! controllare che non serva !!
        piloti_abbinati=[]
        indice_max_piloti_candidati=lista_piloti_candidati.__len__()-1
        
        for i in range(piloti_per_gruppo):
            pilota_candidato=rnd.randint(0,indice_max_piloti_candidati)
            piloti_abbinati.append(lista_piloti_candidati.pop(pilota_candidato))
            indice_max_piloti_candidati-=1
        return piloti_abbinati

    def peso_medio_gruppo(self,diz_piloti,piloti_gruppo):
        numero_piloti_gruppo=piloti_gruppo.__len__()
        peso=0
        for p in piloti_gruppo:
            peso+=diz_piloti[p][0]
        return peso/numero_piloti_gruppo




'''

#Dati piloti iscritti
diz_piloti={1:[10,'Battistella'],2:[30,'Rota'],3:[10,'Rosso'],4:[20,'Giavarini'],
            5:[10,'Surace'],6:[20,'Pompele'],7:[30,'Truffo'],
            8:[15,'Baldelli'],9:[10,'Givone'],10:[12,'Occhibove'],
            11:[18,'Mancini'],12:[8,'Tozzo'],13:[11,'Gualmini'],
            14:[11,'Grandi'],15:[11,'Ciura'] }

totale_piloti = 0
totale_peso=0
lista_piloti_disponibili=[]
limit=0.001
lista_peso_gruppo=[]

#Conto i piloti iscritti, ottengo la somma totale dei pesi dei piloti iscritti, calcolo la media
for p in diz_piloti:
    totale_piloti += 1
    totale_peso+=diz_piloti[p][0]
    lista_piloti_disponibili.append(p)
totale_piloti += 1

peso_medio=totale_peso/totale_piloti
print('\n')
print('Totale piloti: '+str(totale_piloti))
print('Peso medio piloti: '+str(peso_medio))
print('Valore limit: '+str(limit))
print ('limite alto: '+str(peso_medio*(1+limit)))
print ('limite basso: '+str(peso_medio*(1-limit)))
print('\n')
print ('Elenco piloti disponibili:')

for p in lista_piloti_disponibili:
    print (str(p)+" " + str(diz_piloti[p][1]))



# Abbinamenti gruppi task
print('\n')
print('Calcolo Abbinamenti task......')

def abbinamenti(lista_piloti_candidati,piloti_per_gruppo):
    if lista_piloti_candidati.__len__()==piloti_per_gruppo:
        return lista_piloti_candidati
    piloti_abbinati=[]
    indice_max_piloti_candidati=lista_piloti_candidati.__len__()-1
    
    for i in range(piloti_per_gruppo):
        pilota_candidato=rnd.randint(0,indice_max_piloti_candidati)
        piloti_abbinati.append(lista_piloti_candidati.pop(pilota_candidato))
        indice_max_piloti_candidati-=1
    return piloti_abbinati

def peso_medio_gruppo(diz_piloti,piloti_gruppo):
    numero_piloti_gruppo=piloti_gruppo.__len__()
    peso=0
    for p in piloti_gruppo:
        peso+=diz_piloti[p][0]
    return peso/numero_piloti_gruppo

def stampa_piloti(diz_piloti,lista_piloti):
    nominativi_piloti=[]
    for p in lista_piloti:
        nominativi_piloti.append(str(diz_piloti[p][1]+' peso: '+str(diz_piloti[p][0])))
    return nominativi_piloti

while True:
    gruppi_task={}
    lista_piloti_candidati=[]
    lista_piloti_candidati=[p for p in lista_piloti_disponibili]

    for g in range(1,4):
        ultima_task_valida=False
        if g==3: #se ultimo gruppo non genero i numeri random
            piloti_gruppo=abbinamenti(lista_piloti_candidati,5)
            pm=peso_medio_gruppo(diz_piloti,piloti_gruppo)

            if (peso_medio*(1-limit)) < pm < (peso_medio*(1+limit)): # se l'ultimo gruppo è conforme hai limiti
                gruppi_task[g]=piloti_gruppo
                ultima_task_valida=True
                break
            else :
                break
        
        for i in range(10000) :
            piloti_gruppo=abbinamenti(lista_piloti_candidati,5)
            pm=peso_medio_gruppo(diz_piloti,piloti_gruppo)

            if (peso_medio*(1-limit)) < pm < (peso_medio*(1+limit)):
                gruppi_task[g]=piloti_gruppo
                break
            else :
                for p in piloti_gruppo:
                    lista_piloti_candidati.append(p)
                    
    if ultima_task_valida == True: # se anche l'ultima generazione è andata a buon fine  ho finito gli abbinamenti 
        break
    else:
        limit+=0.0001

for k in gruppi_task :
    print ("Gruppo: "+str(k))
    for e in stampa_piloti(diz_piloti,gruppi_task[k]):
       print (e)
    print('\n')
    print ("peso medio gruppo: "+str(peso_medio_gruppo(diz_piloti,gruppi_task[k])))
    print('\n')
    '''