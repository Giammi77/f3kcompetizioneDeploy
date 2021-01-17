from gnr.core.gnrdecorator import metadata
#gnrdbsetup -u
class Table(object):
    def config_db(self, pkg):
        tbl = pkg.table('task_group', pkey='code', name_long='!![en]Task group', 
                        name_plural='!![en]Task groups',caption_field='description',lookup=True)
        self.sysFields(tbl,id=False)
        tbl.column('code' ,size='1',name_long='!![en]Group',validate_case='u',validate_notnull=True)
        tbl.column('description',name_long='!![en]Description',validate_case='u')
        tbl.column('announcement', size=':50', name_long='!![en]Announcement')


    @metadata(mandatory=True)
    def sysRecord_A(self):
        return self.newrecord(code='1',
                            description='A',
                            announcement='GROUP 1')

    @metadata(mandatory=True)
    def sysRecord_B(self):
        return self.newrecord(code='2',
                            description='B',
                            announcement='GROUP 2')

    @metadata(mandatory=True)
    def sysRecord_C(self):
        return self.newrecord(code='3',
                            description='C',
                            announcement='GROUP 3')
    @metadata(mandatory=True)
    def sysRecord_D(self):
        return self.newrecord(code='4',
                            description='D',
                            announcement='GROUP 4')

    @metadata(mandatory=True)
    def sysRecord_E(self):
        return self.newrecord(code='5',
                            description='E',
                            announcement='GROUP 5')

    @metadata(mandatory=True)
    def sysRecord_F(self):
        return self.newrecord(code='6',
                            description='F',
                            announcement='GROUP 6')

    @metadata(mandatory=True)
    def sysRecord_G(self):
        return self.newrecord(code='7',
                            description='G',
                            announcement='GROUP 7')