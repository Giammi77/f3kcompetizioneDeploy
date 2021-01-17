from gnr.core.gnrdecorator import metadata
class Table(object):
    def config_db(self, pkg):
        tbl = pkg.table('task', pkey='code', name_long='!![en]Task', 
                        name_plural='!![en]Tasks',caption_field='description',lookup=True)
        self.sysFields(tbl,id=False)
        tbl.column('code' ,size=':3',name_long='!![it]Task',validate_case='u',validate_notnull=True)
        tbl.column('description',name_long='!![en]Description',validate_case='u')
        tbl.column('operative_time', dtype='N', name_long='!![en]Operative Time', name_short='O.T.')
        tbl.column('announcement', name_long='!![en]Annuncement')
        tbl.column('file_name', name_long='!![en]File name for .mp3')
        tbl.column('glider_score_string', name_long='!![en]Glider Score String')
        tbl.column('timer_code', size='20', name_long='!![en]Timer Code')
    @metadata(mandatory=True)
    def sysRecord_A(self):
        return self.newrecord(code='A',
                            description='TASK A - LAST FLIGHT,  MAX 300 SECONDS O.T 10 MIN.',
                            operative_time=10,
                            announcement='Task A - Last flight counts; 5 min max; Unlimited flights in 10 mins',
                            file_name='F3KTask_A(1).mp3',
                            glider_score_string='A(1)|A(1) - L1 5max in 10m|1',
                            timer_code='F3K-3m10m30s')

    @metadata(mandatory=True)
    def sysRecord_A2(self):
        return self.newrecord(code='A2',
                            description='TASK A2 - LAST FLIGHT,  MAX 300 SECONDS O.T 7 MIN.',
                            operative_time=7,
                            announcement='Task A - Last flight counts; 5 min max; Unlimited flights in 7 mins',
                            file_name='F3KTask_A(2).mp3',
                            glider_score_string='A(2)|A(2) - L1 5max in 7m|1',
                            timer_code='F3K-3m7m30s')

    @metadata(mandatory=True)
    def sysRecord_B(self):
        return self.newrecord(code='B',
                            description='TASK B - NEXT TO LAST AND LAST FLIGHT, MAX 240 SECONDS O.T.10 MIN.',
                            operative_time=10,
                            announcement='Task B - Last 2 flights count; 4 min max; Unlimited flights in 10 mins',
                            file_name='F3KTask_B(1).mp3',
                            glider_score_string='B(1)|B(1) - L2 4max in 10m|1',
                            timer_code='F3K-3m10m30s')

    @metadata(mandatory=True)
    def sysRecord_B2(self):
        return self.newrecord(code='B2',
                            description='TASK B2 - NEXT TO LAST AND LAST FLIGHT, MAX 180 SECONDS O.T.7 MIN.',
                            operative_time=7,
                            announcement='Task B - Last 2 flights count; 3 min max; Unlimited flights in 7 mins',
                            file_name='F3KTask_B(2).mp3',
                            glider_score_string='B(2)|B(2) - L2 3max in 7m|1',
                            timer_code='F3K-3m7m30s')

    @metadata(mandatory=True)
    def sysRecord_C(self):
        return self.newrecord(code='C',
                            description='TASK C - ALL UP, LAST DOWN  MAX 180 SECONDS FOR 3 TIMES',
                            operative_time=3,
                            announcement='Task C - All up; 3 min max; 3 flights per round',
                            file_name='F3KTask_C(1).mp3',
                            glider_score_string='C(1)|C(1) - AllUp 3:00*3|3',
                            timer_code='F3K-1m3m30s')

    @metadata(mandatory=True)
    def sysRecord_C2(self):
        return self.newrecord(code='C2',
                            description='TASK C2 - ALL UP, LAST DOWN  MAX 180 SECONDS FOR 7 TIMES',
                            operative_time=3,
                            announcement='Task C - All up; 3 min max; 4 flights per round',
                            file_name='F3KTask_C(2).mp3',
                            glider_score_string='C(2)|C(2) - AllUp 3:00*4|4',
                            timer_code='F3K-1m3m30s')

    @metadata(mandatory=True)
    def sysRecord_C3(self):
        return self.newrecord(code='C3',
                            description='TASK C3 - ALL UP, LAST DOWN  MAX 180 SECONDS FOR 5 TIMES',
                            operative_time=3,
                            announcement='Task C - All up; 3 min max; 5 flights per round',
                            file_name='F3KTask_C(3).mp3',
                            glider_score_string='C(3)|C(3) - AllUp 3:00*5|5',
                            timer_code='F3K-1m3m30s')


    @metadata(mandatory=True)
    def sysRecord_D(self):
        return self.newrecord(code='D',
                            description='TASK D - TWO FLIGHTS MAX 300 SECONDS O.T. 10 MIN.',
                            operative_time=10,
                            announcement='Task D; Two flights in 10 mins; 5 minute maximum',
                            file_name='F3KTask_D.mp3',
                            glider_score_string='D(1)|D - 2 flights 5max|1',
                            timer_code='F3K-3m10m30s')
                
    @metadata(mandatory=True)
    def sysRecord_E(self):
        return self.newrecord(code='E',
                            description='TASK E (POKER - UP TO 3 TARGET TIMES) O.T. 10 MIN.',
                            operative_time=10,
                            announcement='Task E; Poker; Unlimited flights in 10 minutes; Pilot chooses target times; 3 flights to time count',
                            file_name='F3KTask_E.mp3',
                            glider_score_string='E(1)|E - Poker 3 in 10m|1',
                            timer_code='F3K-3m10m30s')

    @metadata(mandatory=True)
    def sysRecord_E2(self):
        return self.newrecord(code='E2',
                            description='TASK E2 (POKER - UP TO 3 TARGET TIMES) O.T. 15 MIN.',
                            operative_time=15,
                            announcement='Task E; Poker; Unlimited flights in 15 minutes; Pilot chooses target times; 3 flights to time count',
                            file_name='F3KTask_E(2).mp3',
                            glider_score_string='E(2)|E - Poker 3 in 15m|1',
                            timer_code='F3K-3m15m30s')

    @metadata(mandatory=True)
    def sysRecord_F(self):
        return self.newrecord(code='F',
                            description='TASK F (3 OUT OF 6) MAX 180 S. O.T. 10 MIN',
                            operative_time=10,
                            announcement='Task F - 3 longest count; 3 min max; Max 6 flights in 10 mins',
                            file_name='F3KTask_F.mp3',
                            glider_score_string='F|F - Best3 3:00max|1',
                            timer_code='F3K-3m10m30s')

    @metadata(mandatory=True)
    def sysRecord_G(self):
        return self.newrecord(code='G',
                            description='TASK G (FIVE LONGEST FLIGHTS) 5X2 O.T. 10 MIN',
                            operative_time=10,
                            announcement='Task G - 5 longest count; 2 min max; Unlimited flights in 10 min',
                            file_name='F3KTask_G.mp3',
                            glider_score_string='G|G - Best5 2:00max|1',
                            timer_code='F3K-3m10m30s')
                
    @metadata(mandatory=True)
    def sysRecord_H(self):
        return self.newrecord(code='H',
                            description='TASK H (ONE, TWO, THREE AND FOUR MINUTE TARGET FLIGHT TIMES, ANY ORDER) O.T. 10 MIN',
                            operative_time=10,
                            announcement='Task H - Best 4 count; 1, 2, 3 and 4 minutes (any order); Unlimited flights in 10 mins',
                            file_name='F3KTask_H.mp3',
                            glider_score_string='H|H - 1, 2, 3, 4|1',
                            timer_code='F3K-3m10m30s')
            
    @metadata(mandatory=True)
    def sysRecord_I(self):
        return self.newrecord(code='I',
                            description='TASK I (THREE LONGEST FLIGHTS) MAX 200 S. O.T. 10 MIN',
                            operative_time=10,
                            announcement='Task I - Best 3 count; 3:20 max; Unlimited flights in 10 mins',
                            file_name='F3KTask_I.mp3',
                            glider_score_string='I|I - Best3 3:20max|1',
                            timer_code='F3K-3m10m30s')

    @metadata(mandatory=True)
    def sysRecord_J(self):
        return self.newrecord(code='J',
                            description='TASK J (THREE LAST FLIGHTS) MAX 180 S. O.T. 10 MIN',
                            operative_time=10,
                            announcement='Task J - Last 3 count; 3 min max; Unlimited flights in 10 mins',
                            file_name='F3KTask_J.mp3',
                            glider_score_string='J|J - L3 3:00max|1',
                            timer_code='F3K-3m10m30s')
                
    @metadata(mandatory=True)
    def sysRecord_K(self):
        return self.newrecord(code='K',
                            description='TASK K (INCREASING TIME BY 30 SECONDS, “BIG LADDER”) O.T 10 MIN',
                            operative_time=10,
                            announcement='Task K - Big Ladder; 5 flights in order; First target 1 minute; 30 seconds added after each launch',
                            file_name='F3KTask_K.mp3',
                            glider_score_string='K|K - Big Ladder|1',
                            timer_code='F3K-3m10m30s')

    @metadata(mandatory=True)
    def sysRecord_L(self):
        return self.newrecord(code='L',
                            description='TASK L (ONE FLIGHT) MAX 599 S O.T. 10 MIN',
                            operative_time=10,
                            announcement='Task L; One Flight; Maximum time 9 minutes 59 seconds',
                            file_name='F3KTask_L.mp3',
                            glider_score_string='L|L - 1 flight 9:59max|1',
                            timer_code='F3K-3m10m30s')

    @metadata(mandatory=True)
    def sysRecord_M(self):
        return self.newrecord(code='M',
                            description='FLY-OFF TASK M (INCREASING TIME BY 2 MINUTES “HUGE LADDER”) 3-5-7 O.T. 15 MIN',
                            operative_time=15,
                            announcement='Task M; Huge Ladder; 3, 5 and 7 minute flights in 15 minutes; 3 flights maximum',
                            file_name='F3KTask_M.mp3',
                            glider_score_string='M|M - Huge Ladder|1',
                            timer_code='F3K-3m15m30s')