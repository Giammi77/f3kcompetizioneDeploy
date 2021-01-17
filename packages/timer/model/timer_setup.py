# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl=pkg.table('timer_setup', pkey='id', name_long='!![en]Timer Setup', name_plural='!![en]Timer Setups'
                        ,caption_field='timer_name')
        self.sysFields(tbl)
        tbl.column('timer_code', size='20', 
                    name_long='!![en]Timer Name').relation('timer.timer.code',
                                                    relation_name='timer_setup',
                                                    mode='foreingkey',
                                                    onDelete='raise')
        tbl.column('timer_time', dtype='N', name_long='!![en]Timer Time')
        tbl.column('display_time', size='5', name_long='!![en]Display Time')
        tbl.column('timer_state_code', size='2'
                    , name_long='!![en]Timer State').relation('timer.timer_state.code',
                                                    relation_name='timer_setup',
                                                    mode='foreingkey',
                                                    onDelete='raise')
        tbl.column('on_new_round', dtype='B', name_long='!![en]On New Round')
        tbl.column('announcement', size=':100', name_long='!![en]Announcement')
        tbl.column('announcement_file_name', size=':100', name_long='!![en]Announcement File Name')
        tbl.column('beep_frequency', dtype='L', name_long='!![en]Beep Frequency (Hz)')
        tbl.column('beep_duaration', dtype='L', name_long='!![en]Beep Duration (Msecs)')
