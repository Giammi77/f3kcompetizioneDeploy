from gnr.web.batch.btcaction import BaseResourceAction
import f3kvoice as voice
import os
caption='Make Play List' #nome del menu del batch
tags='admin' #autorizzazione al batch
description='Make play list for the competition' #nome più completo

class Main(BaseResourceAction):
    batch_prefix = 'AS'
    batch_title = 'Make Play List'
    batch_cancellable=True
    
    def do(self):
        # sn = self.site.storageNode('site:voices')
        # path = sn.internal_path

        tbl_audio=self.db.table('timer.audio')

        tbl_registration=self.db.table('f3kp.registration')
        tbl_task=self.db.table('f3kp.task')
        tbl_task_group=self.db.table('f3kp.task_group')

        tbl_competition_task=self.db.table('f3kp.competition_task')
        tbl_combination=self.db.table('f3kp.combination')

        #per ottentere i valori dei parametri richiersti self.batch_parameters
        #per ottenere i record selezionati s=get_selection poi s.data()
        #
        #OTTENGO id delle competition 
 

        selection=self.get_selection(columns='id,audio_path')
        play_list=['~ F3K']
        F3KF5KTaskByRound=[]
        audio_list=[]
        if not selection:
            return
        #PER OGNI id 
        for e in selection:
            competition_id=e.get('id').strip()
            audio_path=e.get('audio_path').replace(' ','') #.strip()
            competition_tasks=tbl_competition_task.query(columns="""$competition_id,
                    $_row_count,
                    $task_code_file_name,
                    $task_code_announcement,
                    $glider_score_string,
                    $timer_code,
                    $number_groups""",where='$competition_id=:competition_id',
                                    competition_id=competition_id,order_by='$_row_count ASC').fetch()


            for competition_task in competition_tasks:
                task_number=competition_task['_row_count']
                number_groups=competition_task['number_groups']
                task_code_file_name=competition_task['task_code_file_name']
                task_code_announcement=competition_task['task_code_announcement']
                timer_code=competition_task['timer_code']
                glider_score_string=competition_task['glider_score_string']
                F3KF5KTaskByRound.append(str(task_number)+'|'+glider_score_string)
                
                for i in range(number_groups):
                    # ##Round 1   Group 1   ReFlight 0
                    starter='## Round '+str(task_number)+'   Group '+str(i)+'   ReFlight 0'
                    play_list.append(starter)

                    # C:\GliderScore6\Audio\Round1.wav
                    
                    announcement='Round '+str(task_number)
                    file_name=announcement.replace(' ','')+'.mp3'
                    play_list.append(audio_path+file_name)
                    audio_list.append((announcement,file_name))
                    f=tbl_audio.query(columns='file_name',
                    where='$file_name= :file_name',file_name=file_name).fetch()
                    if not f:
                        new_record=tbl_audio.newrecord(
                                                    description=announcement,
                                                    phonetic=announcement,
                                                    file_name=file_name,
                                                    audio_type='ROUND')
                        
                        tbl_audio.insert(new_record)
                        self.db.commit()

                    # C:\GliderScore6\Audio\Group1.wav
                    announcement='Group '+str(i+1)
                    file_name=announcement.replace(' ','')+'.mp3'
                    play_list.append(audio_path+file_name)
                    audio_list.append((announcement,file_name))
                    f=tbl_audio.query(columns='file_name',
                    where='$file_name= :file_name',file_name=file_name).fetch()
                    if not f:
                        new_record=tbl_audio.newrecord(
                                                    description=announcement,
                                                    phonetic=announcement,
                                                    file_name=file_name,
                                                    audio_type='GROUP')
                        
                        tbl_audio.insert(new_record)
                        self.db.commit()

                    # C:\GliderScore6\Audio\F3KTask_A(1).wav
                    play_list.append(audio_path+task_code_file_name)
                    audio_list.append((task_code_announcement,task_code_file_name))
                    

                    #C:\GliderScore6\Audio\ZZHoudalakis_Jim.wav
                    
                    combinations=tbl_combination.query(columns='$announcement_name',
                                        where='$competition_id=:competition_id AND $task_group_code=:group_number',
                                        competition_id=competition_id,
                                        group_number=str(i+1)).fetch()
                           
                    
                    for pilot in combinations:
                        announcement=pilot['announcement_name']
                        announcement_file_name=announcement.replace(' ','')+'.mp3'
                        play_list.append(audio_path+announcement_file_name)
                        audio_list.append((announcement,announcement_file_name))
                        f=tbl_audio.query(columns='file_name',
                            where='$file_name= :announcement_file_name',announcement_file_name=announcement_file_name).fetch()
                        if not f: 
                            new_record=tbl_audio.newrecord(
                                                        description=announcement,
                                                        phonetic=announcement,
                                                        file_name=announcement_file_name,
                                                        audio_type='PILOT')
                            
                            tbl_audio.insert(new_record)
                            self.db.commit()

                    # #Timer F3K-3m10m30s
                    #glider_score_string='A(2)|A(2) - L1 5max in 7m|1'
                    #timer_code='F3K-3m7m30s'
                    rep=int(glider_score_string[-1])
                    
                    for r in range(rep):
                        if rep >1:
                            timer_code='F3K-3m10m30s'
                        if r >=1:
                            timer_code='F3K-1m3m30s'
                        play_list.append('#Timer '+timer_code)

                        

                        setup=self.db.table('timer.timer_setup').query(where='$timer_code=:timer_code',timer_code=timer_code,order_by='$timer_time ASC').fetch()
                        
                        for s in setup:
                            # -183|3:03|PT|C:\GliderScore6\Audio\WorkingTimeIn-3Mins.wav|0|0
                            timer_time=s.get('timer_time')
                            display_time=s.get('display_time').strip()
                            timer_state_code=s.get('timer_state_code')
                            announcement_file_name=s.get('announcement_file_name')
                            announcement=s.get('announcement')
                            if s.get('announcement_file_name'):
                                if announcement:
                                    audio_list.append((announcement,announcement_file_name))
                                announcement_file_name= audio_path+announcement_file_name
                            else:
                                announcement_file_name=s.get('announcement_file_name')
                            beep_frequency=s.get('beep_frequency')
                            beep_duaration=s.get('beep_duaration')
                            
                            str_setup=str(timer_time)+'|'+display_time+'|'+timer_state_code+'|'+announcement_file_name+'|'+str(beep_frequency)+'|'+str(beep_duaration)
                            play_list.append(str_setup)
                    # #End of Timer
                    play_list.append('#End of Timer')   
            str_play_list=''
            for p in play_list:
                str_play_list+=p+'\n'
            tbl_competition=self.db.table('f3kp.competition')
            
            with tbl_competition.recordToUpdate(competition_id) as rec:
                rec['play_list'] = str_play_list      
            self.db.commit()

            sn = self.page.site.storageNode('site:GliderScoreDigitalPlayList.m3u')

            out_file = open((sn.internal_path),"w")
            for p in play_list:
                out_file.write(p+'\n')
            out_file.close()

            for a in audio_list:
                sn = self.page.site.storageNode('site:'+str(a[1]))
                voice.create_voice(a[0],sn.internal_path)
                
            sn = self.page.site.storageNode('site:F3KF5KTaskByRound.txt')
            
            out_file = open((sn.internal_path),"w")
            for p in F3KF5KTaskByRound:
                out_file.write(p+'\n')
            out_file.close()

