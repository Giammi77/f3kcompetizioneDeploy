# encoding: utf-8
import f3krules as rules

class Table(object):
    def config_db(self,pkg):
        tbl=pkg.table('flight_time', pkey='id', name_long='!![en]Flight time', name_plural='!![en]Flight times',
                        caption_field='combination_id')
        self.sysFields(tbl,counter='combination_id')
        tbl.column('combination_id', size='22', name_long='!![en]Combination', name_short='Combinations'
                    ).relation('combination.id',
                                relation_name='flight_time',
                                mode='foreingkey',
                                onDelete='cascade')
        tbl.column('flight_time', dtype='N', name_long='!![en]Flight time')
        tbl.aliasColumn('task_code','@combination_id.@competition_task_id.task_code')
        tbl.formulaColumn('minutes','CASE WHEN $flight_time = 0 THEN null ELSE trunc($flight_time/60) END')
        tbl.formulaColumn('seconds','CASE WHEN $flight_time = 0 THEN null ELSE trunc($flight_time-trunc($flight_time/60)*60) END')
        tbl.formulaColumn('tenths','CASE WHEN $flight_time = 0 THEN null ELSE ($flight_time-trunc($flight_time))*10 END')


    def trigger_onInserting(self, record=None):

        rule={'A':rules.A(),'A2':rules.A2(),'B':rules.B(),'B2':rules.B2(),
            'C':rules.C(),'C2':rules.C2(),'D':rules.D(),'E':rules.E(),
            'E2':rules.E2(),'F':rules.F(),'G':rules.G(),'H':rules.H(),
            'I':rules.I(),'J':rules.J(),'K':rules.K(),'L':rules.L(),
            'M':rules.M()}
        combination_id=record['combination_id']
        combination = self.db.table('f3kp.combination').record(combination_id,mode='bag')
        task=combination['@competition_task_id.task_code'] 
        r=rule[task]

        flyed_time= self.db.table('f3kp.flight_time').query(columns='$combination_id,$flight_time',
                            where='$combination_id= :combination_id',
                            combination_id=combination_id).fetch()
        flyed=0
        number_flights=0
        for f in flyed_time:
            number_flights+=1
            flyed+=f['flight_time']
  
        if number_flights<r.maximum_flights:
            record['save']=True
        else:
            record['save']=False

        if record['flight_time'] :# this case occur when flight-time is inserted from mobile
            record['flight_time']=r.validate_flight(record['flight_time'],flyed)
            return

        try:
            minutes=int(record['minutes'])
        except:
            minutes=0
        try:
            seconds=int(record['seconds'])
        except:
            seconds=0
        try:
            tenths=int(record['tenths'])
        except:
            tenths=0
        try:
            flight_time=minutes*60+seconds+tenths/10
            
            record['flight_time']=flight_time
        except:
            record['flight_time']=0
        

        record['flight_time']=r.validate_flight(record['flight_time'],flyed)
        

    def trigger_onUpdating(self, record=None,old_record=None):
        rule={'A':rules.A(),'A2':rules.A2(),'B':rules.B(),'B2':rules.B2(),
            'C':rules.C(),'C2':rules.C2(),'D':rules.D(),'E':rules.E(),
            'E2':rules.E2(),'F':rules.F(),'G':rules.G(),'H':rules.H(),
            'I':rules.I(),'J':rules.J(),'K':rules.K(),'L':rules.L(),
            'M':rules.M()}
        combination_id=record['combination_id']
        combination = self.db.table('f3kp.combination').record(combination_id,mode='bag')
        task=combination['@competition_task_id.task_code'] 
        r=rule[task]

        
        flyed_time= self.db.table('f3kp.flight_time').query(columns='$combination_id,$flight_time,$id',
                            where='$combination_id= :combination_id',
                            combination_id=combination_id).fetch()
        flight_time_id=record['id'] 
        flyed=0
        for f in flyed_time:
            if f['id'] == flight_time_id:
                continue # drop the current fly_time 
            flyed+=f['flight_time'] #this data is used for the validation 
            

        if not old_record: # record['flight_time'] : # this case occur when flight-time is inserted from mobile
            record['flight_time']=r.validate_flight(record['flight_time'],flyed)
            return
        flight_time= old_record['flight_time']
        try:
            old_minutes=int(flight_time/60)
        except:
            old_minutes=0
        try:
            old_seconds=flight_time-(old_minutes*60)
        except:
            old_seconds=0   
        try:
            old_tenths=flight_time/int(flight_time)
        except:
            old_tenths=0
            
        try:
            minutes=int(record['minutes'])
        except:
            minutes=int(old_minutes)
        try:
            seconds=int(record['seconds'])
        except:
            seconds=int(old_seconds)
        try:
            tenths=int(record['tenths'])
        except:
            tenths=int(old_tenths)

        flight_time=minutes*60+seconds+tenths/10

        
        record['flight_time']=r.validate_flight(flight_time,flyed)

        

    def trigger_onInserted(self, record=None ):

        if record['save']==False:         
            id=record['id']
            self.deleteSelection(columns='$id,combination_id',
                                    where='$id=:pref',
                                    pref= id,)
            self.db.commit()
        else:
            combination_id=record['combination_id']
            combination=self.db.table('f3kp.combination')
            combination.upgrade_time_registred(combination_id,True)

    def trigger_onDeleted(self, record=None):
        
        combination_id=record['combination_id']
        check_if_flight_times= self.query(columns='$id,$combination_id',
        where='$combination_id= :combination_id',
        combination_id=combination_id).fetch()
        if len(check_if_flight_times)==0:
            combination=self.db.table('f3kp.combination')
            combination.upgrade_time_registred(combination_id,False)

    def add_flight_time(self,combination_id=None,flight_time=None,*args,**kwargs):
        newFlight=self.newrecord(combination_id=combination_id,
                                        flight_time= flight_time)
        self.insert(newFlight)
        self.db.commit()

    def update_flight_time(self,flight_time_id=None,flight_time=None,*args,**kwargs):
        record=self.record(flight_time_id,mode='bag')
        record['flight_time']=flight_time
        self.update(record)
        self.db.commit()

