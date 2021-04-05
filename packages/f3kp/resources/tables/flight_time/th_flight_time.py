#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method
from gnr.web.gnrwebstruct import struct_method

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('_row_count')
        r.fieldcell('combination_id')
        r.fieldcell('flight_time')

    def th_order(self):
        return 'combination_id'

    def th_query(self):
        return dict(column='combination_id', op='contains', val='')

class ViewFromCombination(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('_row_count',name='Nr.',width='3em')
        r.fieldcell('combination_id',edit=False)
        r.cell('minutes',name='!![en]Minute',edit=dict(edit=True,align='center'),
                        validate_regex="\d",text_align='center')#,remoteRowController=True)

        r.cell('seconds',name='!![en]Second',edit=dict(edit=True,align='center'), 
                        validate_regex="\d",text_align='center')#,remoteRowController=True)
        r.cell('tenths',name='!![en]Tenth',edit=dict(edit=True,align='center'),
                        validate_regex="\d",text_align='center')#),remoteRowController=True)
        r.fieldcell('flight_time',edit=False,totalize=True)
        # r.cell('task_code',name='Task code')

    def th_hiddencolumns(self):
        return "$task_code,$id"
    def th_order(self):
        return 'combination_id'

    def th_query(self):
        return dict(column='combination_id', op='contains', val='')




    # @public_method
    # def th_remoteRowController(self,row=None,field=None,**kwargs):
    #     field = field or 'prodotto_id' #nel caso di inserimento batch il prodotto viene considerato campo primario
    #     if not row['prodotto_id']:
    #         return row
    #     if not row['quantita']:
    #         row['quantita'] = 1
    #     if field == 'prodotto_id':
    #         prezzo_unitario,tipo_iva_codice,aliquota_iva = self.db.table('fatt_a.prodotto'
    #                                 ).readColumns(columns='$prezzo_unitario,@tipo_iva_codice.codice,@tipo_iva_codice.aliquota'
    #                                             ,pkey=row['prodotto_id'])
    #         row['prezzo_unitario'] = prezzo_unitario
    #         row['tipo_iva_codice'] = tipo_iva_codice
    #         row['aliquota'] = aliquota_iva
    #     row['prezzo_totale'] = decimalRound(row['quantita'] * row['prezzo_unitario'])
    #     row['iva'] = decimalRound(old_div(row['aliquota'] * row['prezzo_totale'],100))
    #     return row

class ViewFromPilotMobile(ViewFromCombination):
    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('_row_count',name='N.',width='1.5em',_align='center')
        r.cell('minutes',name='Min',
                        width='3em',text_align='center')
        r.cell('seconds',name='Sec', 
                        width='3em',text_align='center')
        r.cell('tenths',name='!![en]Ten',
                        width='3em',text_align='center')

        r.fieldcell('flight_time',edit=False,totalize=True,width='3em',name='Time')
        # r.cell('task_code',name='Task code')
        r.cell('Delete',calculated=True,format_buttonclass='gear iconbox',
                    format_isbutton=True,
                    format_onclick="""var row = this.widget.rowByIndex($1.rowIndex);
                                      PUBLISH do_action = {flight_time_id:row._pkey};""",
                    width='3em')
    # def th_top_toolbar(self,top):
    #     top.div('ciaooooo')

    def th_view(self,view):
        view.dataRpc('dummy',self.delTime,subscribe_do_action=True,_lockScreen=dict(message='Deleting time'))
        
    @public_method
    def delTime(self,flight_time_id=None):
        tbl_flight_time=self.db.table('f3kp.flight_time')
        tbl_flight_time.delTime(flight_time_id)
        
    def th_top_custom(self,top):
        
        bar=top.bar.replaceSlots('#','2,view_title,*,delrow,2',font_size='20px')
        bar.view_title.div('FLIGHT TIMES') 
        # bar.delrow.style(width='25px',height='25px',layout_width='100dp',layout_height='100dp')
        # bar.edit.button('DELETE',action="genro.bp(true)",font_size='20px',
                        
        #                 )

class Form(BaseComponent):

    def th_form(self, form):
        pane = form.record
        fb = pane.formbuilder(cols=2, border_spacing='4px')
        fb.field('combination_id')
        fb.field('flight_time')


    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px')
