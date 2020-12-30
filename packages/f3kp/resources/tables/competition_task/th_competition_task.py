#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('_row_count',name='Nr.Task')
        r.fieldcell('competition_id')
        r.fieldcell('task_code',edit=dict(edit=True,validate_notnull=True,hasDownArrow=True))
        r.fieldcell('state_code')
        r.fieldcell('number_groups',edit=dict(edit=True,validate_notnull=True))

    def th_order(self):
        return '_row_count'

    def th_query(self):
        return dict(column='', op='contains', val='')

class Viewcompetition_taskFromCompetition(View): 
    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('_row_count',name='Nr.Task')
        r.fieldcell('competition_id')
        r.fieldcell('task_code',edit=dict(edit=True,validate_notnull=True,hasDownArrow=True),
                    width='40em')
        r.fieldcell('state_code',edit=dict(edit=True,hasDownArrow=True,validate_notnull=True,default_value='A'))
        r.fieldcell('number_groups',edit=dict(edit=True,validate_notnull=True,default_value=1))

    def th_top_custom(self,top):
        bar=top.bar.replaceSlots('#','#,resourceActions,2') 
        # bar=top.slotToolbar('*,miobut,*')
        # bar.miobut.button('IMPORTA PRODOTTI',action='genro.publish("importa_prodotti",{selected:selected})',
        #                     selected='=#scelta_tipo.checked')
        # bar.mioPicker.button('Picker Prodotti',action='genro.publish("mostra_picker")')
    

class Form(BaseComponent):

    def th_form(self, form):
        pane = form.record
        fb = pane.formbuilder(cols=2, border_spacing='4px')
        fb.field('competition_id' )
        # fb.field('task_code' )
        # fb.field('end_task' )


    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px' )
