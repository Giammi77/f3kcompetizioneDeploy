from gnr.core.gnrdecorator import metadata
class Table(object):
    def config_db(self, pkg):
        tbl = pkg.table('task', pkey='code', name_long='!![en]Task', 
                        name_plural='!![en]Tasks',caption_field='description',lookup=True)
        self.sysFields(tbl,id=False)
        tbl.column('code' ,size=':3',name_long='!![it]Task',validate_case='u',validate_notnull=True)
        tbl.column('description',name_long='!![en]Description',validate_case='u')
        tbl.column('operative_time', dtype='N', name_long='!![en]Operative Time', name_short='O.T.')
    
    @metadata(mandatory=True)
    def sysRecord_A(self):
        return self.newrecord(code='A',
                            description='TASK A - LAST FLIGHT,  MAX 300 SECONDS O.T 10 MIN.',
                            operative_time=10)

    @metadata(mandatory=True)
    def sysRecord_A2(self):
        return self.newrecord(code='A2',
                            description='TASK A2 - LAST FLIGHT,  MAX 300 SECONDS O.T 7 MIN.',
                            operative_time=7)

    @metadata(mandatory=True)
    def sysRecord_B(self):
        return self.newrecord(code='B',
                            description='TASK B - NEXT TO LAST AND LAST FLIGHT, MAX 240 SECONDS O.T.10 MIN.',
                            operative_time=10)

    @metadata(mandatory=True)
    def sysRecord_B2(self):
        return self.newrecord(code='B2',
                            description='TASK B2 - NEXT TO LAST AND LAST FLIGHT, MAX 180 SECONDS O.T.7 MIN.',
                            operative_time=7)

    @metadata(mandatory=True)
    def sysRecord_C(self):
        return self.newrecord(code='C',
                            description='TASK C - ALL UP, LAST DOWN  MAX 180 SECONDS FOR 3 TIMES',
                            operative_time=3)

    @metadata(mandatory=True)
    def sysRecord_C2(self):
        return self.newrecord(code='C2',
                            description='TASK C2 - ALL UP, LAST DOWN  MAX 180 SECONDS FOR 5 TIMES',
                            operative_time=3)

    @metadata(mandatory=True)
    def sysRecord_D(self):
        return self.newrecord(code='D',
                            description='TASK D - TWO FLIGHTS MAX 300 SECONDS O.T. 10 MIN.',
                            operative_time=10)
                
    @metadata(mandatory=True)
    def sysRecord_E(self):
        return self.newrecord(code='E',
                            description='TASK E (POKER - UP TO 3 TARGET TIMES) O.T. 10 MIN.',
                            operative_time=10)

    @metadata(mandatory=True)
    def sysRecord_E2(self):
        return self.newrecord(code='E2',
                            description='TASK E2 (POKER - UP TO 3 TARGET TIMES) O.T. 15 MIN.',
                            operative_time=15)

    @metadata(mandatory=True)
    def sysRecord_F(self):
        return self.newrecord(code='F',
                            description='TASK F (3 OUT OF 6) MAX 180 S. O.T. 10 MIN',
                            operative_time=10)

    @metadata(mandatory=True)
    def sysRecord_G(self):
        return self.newrecord(code='G',
                            description='TASK G (FIVE LONGEST FLIGHTS) 5X2 O.T. 10 MIN',
                            operative_time=10)
                
    @metadata(mandatory=True)
    def sysRecord_H(self):
        return self.newrecord(code='H',
                            description='TASK H (ONE, TWO, THREE AND FOUR MINUTE TARGET FLIGHT TIMES, ANY ORDER) O.T. 10 MIN',
                            operative_time=10)
            
    @metadata(mandatory=True)
    def sysRecord_I(self):
        return self.newrecord(code='I',
                            description='TASK I (THREE LONGEST FLIGHTS) MAX 200 S. O.T. 10 MIN',
                            operative_time=10)

    @metadata(mandatory=True)
    def sysRecord_J(self):
        return self.newrecord(code='J',
                            description='TASK J (THREE LAST FLIGHTS) MAX 180 S. O.T. 10 MIN',
                            operative_time=10)
                
    @metadata(mandatory=True)
    def sysRecord_K(self):
        return self.newrecord(code='K',
                            description='TASK K (INCREASING TIME BY 30 SECONDS, “BIG LADDER”) O.T 10 MIN',
                            operative_time=10)

    @metadata(mandatory=True)
    def sysRecord_L(self):
        return self.newrecord(code='L',
                            description='TASK L (ONE FLIGHT) MAX 599 S O.T. 10 MIN',
                            operative_time=10)

    @metadata(mandatory=True)
    def sysRecord_M(self):
        return self.newrecord(code='M',
                            description='FLY-OFF TASK M (INCREASING TIME BY 2 MINUTES “HUGE LADDER”) 3-5-7 O.T. 15 MIN',
                            operative_time=15)