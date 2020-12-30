# encoding: utf-8
from gnr.core.gnrdecorator import public_method
class Table(object):
    def config_db(self,pkg):
        tbl=pkg.table('competition', pkey='id', name_long='!![en]Competition', name_plural='!![en]Competitions'
                        ,caption_field='name_competition')
        self.sysFields(tbl)
        tbl.column('name', size=':30', name_long='!![en]Name',validate_case='u')
        tbl.column('venue', size=':30', name_long='!![en]Venue',validate_case='u')
        tbl.column('date', dtype='D', name_long='!![en]Date')
        tbl.column('state_code', size='1', name_long='!![en]State').relation('state.code',
                                relation_name='competition')
        tbl.column('short_note',size=':255',name_long='!![en]Short Note')
        tbl.column('competition_informations', name_long='!![en]Info', name_short='Competition informations')
        tbl.column('preparation_time', dtype='N', name_long='!![en]Preparation time',validate_notnull=True)# lo fa' in tutte le form e view?
        tbl.formulaColumn('name_competition', "$name || ' ' || $date",name_long='!![en]Competition') 
      
    def defaultValues(self):
        return dict(preparation_time=5)

