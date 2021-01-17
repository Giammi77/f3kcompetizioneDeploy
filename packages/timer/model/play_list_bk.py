# encoding: utf-8
# DA VALUTARE SE FARE UNA TABELLA OPPURE UN CAMPO SOLO NELLA TABELLA COMPETITION 
#
# PER ORA HO MESSO UN CAMPO 'play_list' NELLA TABELLA COMPETITION


class Table(object):
    def config_db(self,pkg):
        tbl=pkg.table('play_list', pkey='id', name_long='!![en]Play List', name_plural='!![en]Play Lists'
                        ,caption_field='competition_name')
        self.sysFields(tbl)
        
        tbl.column('competition_id', size='22',
                    name_long='!![en]Competition').relation('f3kp.competition.id',
                                                        relation_name='play_list',
                                                        mode='foreingkey',
                                                        onDelete='cascade')
                  
        tbl.column('text_play_list',name_long='!![en]Text Play List')
        tbl.aliasColumn('competition_name','@competition_id.name_competition')