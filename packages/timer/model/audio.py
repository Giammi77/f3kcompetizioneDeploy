# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl=pkg.table('audio', pkey='id', name_long='!![en]Audio ', name_plural='!![en]Audio',caption_field='description')
        self.sysFields(tbl)
        tbl.column('description', size=':100', name_long='!![en]Description')
        tbl.column('phonetic', size=':100', name_long='!![en]Phonetic')
        tbl.column('file_name', size=':100', name_long='!![en]File name')
        tbl.column('audio_type', size='15',
                    name_long='!![en]Audio type').relation('timer.audio_type.code',
                                                    relation_name='audio',
                                                    mode='foreingkey',
                                                    onDelete='cascade')
    
