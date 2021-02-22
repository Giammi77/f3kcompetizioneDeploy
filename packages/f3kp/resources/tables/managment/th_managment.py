#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method
from time import time,sleep

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('competition_task_id',width='35em')
        r.fieldcell('competition_task_row_count',name='!![en]Task Nr.')
        r.fieldcell('task_group_code',width='5em')
        r.fieldcell('operative_time',edit=dict(edit=True))
        r.fieldcell('preparation_time',edit=dict(edit=True))
        # r.fieldcell('time_end',width='5em',edit=True)
        r.cell('time2_end',calculated=True,
          _customGetter="function(row){if (row.time_end ==0){return '';} else {return new Date(row.time_end).toLocaleString();}}",
          name='!![en]Time end',text_align='left')
    
        # r.checkboxcolumn('activated',width='5em',edit=dict(edit=True),radioButton=True)
        r.checkboxcolumn('activated',width='5em')
    def th_hiddencolumns(self):
        return "$time_end"


    def th_top_custom(self,top):
        # top.data('.timer','None',serverpath='timer')
        # action='1:Run Only activated Task,2:Run all from the start,3:Run all from the activated Task'
        bar=top.bar.replaceSlots('#','*,delrow,resourceActions,2') 

        # bar.cbo_task.formbuilder(cols=1).dbselect('^.task',dbtable='f3kp.managment',
        #                         lbl='Task',rowcaption='$managment_description',columns='$id',
        #                         condition='$competition_id=:competition_id',
        #                         condition_competition_id='^#FORM.pkey',hasDownArrow=True,width='25em')

        # bar.cbo_action.formbuilder(cols=1).filteringSelect('^.action',lbl='Action',
        #                values=action,edit=dict(edit=True))
        # bar.bt_run.button('Run', action='FIRE .run')
        # bar.timer.div('^.timer')
        # bar=top.slotToolbar('*,miobut,*')
        # bar.miobut.button('IMPORTA PRODOTTI',action='genro.publish("importa_prodotti",{selected:selected})',
        #                     selected='=#scelta_tipo.checked')
        # bar.mioPicker.button('Picker Prodotti',action='genro.publish("mostra_picker")')
        # top.dataRpc('.py_time_end',self.run_action_managment,fire='^.run',action='=.action',competition_id='=#FORM.pkey',
        #             task='=.task')
        # top.dataRpc('.timer',self.upgrade_timer,action='=.action',competition_id='=#FORM.pkey',task='=.task',
        #             py_time_end='^.py_time_end',_delay=100)          

    def th_order(self):
        return 'competition_task_row_count,task_group_code'

    def th_query(self):
        return dict(column='competition_task_id', op='contains', val='')

    # @public_method
    # def run_action_managment(self,fire=None,action=None,competition_id=None,task=None,**kwargs):
        
    #     if not fire or not action or not task:
    #         return
    #     #action='1:Run Only activated Task,2:Run all from the start,3:Run all from the activated Task'
    #     if action == '1' :
    #         record_managment=self.db.table('f3kp.managment').query(columns='$id,$operative_time,$preparation_time',
    #                                         where='$competition_id=:competition_id AND $id=:id',
    #                                         competition_id=competition_id,
    #                                         id=task
    #                                         ).fetch()
            
    #         operative_time=record_managment[0]['operative_time']
    #         preparation_time=record_managment[0]['preparation_time']
    #         task_time=operative_time+preparation_time
    #         py_time_end=time()+int(task_time)
    #         time_end=py_time_end*1000
    #         id=record_managment[0]['id']
            
    #         records_managment=self.db.table('f3kp.managment').query(columns='$id,$activated',
    #                                         where='$competition_id=:competition_id',
    #                                         competition_id=competition_id
    #                                         ).fetch()

    #         for r in records_managment:
    #             mangment_id=r['id']
    #             with self.db.table('f3kp.managment').recordToUpdate(mangment_id) as rec:
    #                 rec['activated'] = False
    #                 rec['time_end']= 0
    #             self.db.commit()

    #         with self.db.table('f3kp.managment').recordToUpdate(id) as rec:
    #             rec['time_end'] = time_end
    #             rec['activated'] = True
    #         self.db.commit()
            
    #         return py_time_end
        

    # @public_method
    # def upgrade_timer(self,py_time_end,action=None,competition_id=None,task=None,**kwargs):
    #     if py_time_end:
    #         id=self.db.table('f3kp.managment').query(columns='$id,$operative_time,$preparation_time',
    #                                         where='$competition_id=:competition_id AND $id=:id',
    #                                         competition_id=competition_id,
    #                                         id=task
    #                                         ).fetch()[0]['id']

    #         now=time()
    #         while now<py_time_end :
    #             now=time()
            
    #         with self.db.table('f3kp.managment').recordToUpdate(id) as rec:
    #             rec['time_end'] = 0
    #             rec['activated'] = False
    #         self.db.commit()
            
    #         return py_time_end

    #     else:
    #         return 

class ViewFromContestPageMobile(View):
    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('competition_task_id',width='15em')
        r.fieldcell('competition_task_row_count',name='!![en]Task Nr.',width='3em')
        r.fieldcell('task_group_code',width='3em')
        r.fieldcell('operative_time',edit=dict(edit=True),width='3em')
        r.fieldcell('preparation_time',edit=dict(edit=True),width='3em')
        # r.fieldcell('time_end',width='5em',edit=True)
        r.cell('time2_end',calculated=True,
          _customGetter="function(row){if (row.time_end ==0){return '';} else {return new Date(row.time_end).toLocaleString();}}",
          name='!![en]Time end',text_align='left')
        r.checkboxcolumn('activated',width='5em',edit=dict(edit=False))


    def th_top_custom(self,top):
        # top.data('.timer','None',serverpath='timer')
        # action='1:Run Only activated Task,2:Run all from the start,3:Run all from the activated Task'
        bar=top.bar.replaceSlots('#','*,delrow,resourceActions,2',display='inline-block') 

class ViewFromPilotPageMobile(View):
    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('competition_task_id',width='15em')
        r.fieldcell('competition_task_row_count',name='!![en]Task Nr.',width='3em')
        r.fieldcell('task_group_code',width='3em')
        r.fieldcell('activated',width='5em',name='!![en]Current Task',edit=False)


class Form(BaseComponent):

    def th_form(self, form):
        pane = form.record
        fb = pane.formbuilder(cols=2, border_spacing='4px')
        fb.field('competition_task_id')
        # fb.field('state_code')
        fb.field('task_group_code')


    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px')
