# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl=pkg.table('pilot', pkey='id', name_long='!![en]Pilot', name_plural='!![en]Pilots',caption_field='full_name')
        self.sysFields(tbl)
        tbl.column('first_name', size=':60', name_long='!![en]First Name',validate_case='u')
        tbl.column('last_name', size=':60', name_long='!![en]Last Name',validate_case='u')
        tbl.column('fai_number', size=':15', name_long='!![en]FAI Number', name_short='!![en]FAI Numbers',validate_case='u')
        tbl.column('other_regist_number', size=':15', name_long='!![en]Other Registration Number',
                    name_short='!![en]Other Reg. Nr.',validate_case='u')
        tbl.column('fai_id', size=':15', name_long='!![en]FAI Id',validate_case='u')
        tbl.column('pilot_class', size=':20', name_long='!![en]Pilot Class',validate_case='u')
        tbl.column('club', size=':60', name_long='!![en]Club',validate_case='u')
        tbl.column('street', size=':30', name_long='!![en]Street',validate_case='u')
        tbl.column('town', size=':30', name_long='!![en]Town',validate_case='u')
        tbl.column('state', size=':15', name_long='!![en]State',validate_case='u')
        tbl.column('post_code', size=':8', name_long='!![en]Post Code',validate_case='u')
        tbl.column('country', size='2', name_long='!![en]Country',validate_case='u')
        tbl.column('email', size=':60', name_long='E@mail',validate_regex='[A-z0-9\.\+_-]+@[A-z0-9\._-]+\.[A-z]{2,6}')

        tbl.column('private_phone', size=':18', name_long='!![en]Private Phone', name_short='!![en]Pvt. Phone')
        tbl.column('work_phone', size=':18', name_long='!![en]Work Phone', name_short='!![en]Wrk.')

        tbl.column('user_id',size='22', group='_', name_long='!![en]User',unique=True
            ).relation('adm.user.id',one_one=True, 
                    relation_name='student', 
                    mode='foreignkey', onDelete='raise')

        tbl.formulaColumn('full_name', "$last_name || ' ' || LEFT($first_name,1) || '.'",name_long='!![en]Full Name') 
        

    def createPilot(self,user_record):
        if self.checkDuplicate(user_id=user_record['id']):
            #existing student with the same user_id
            return
        newPilot = self.newrecord(
            first_name = user_record['firstname'],
            last_name = user_record['lastname'],
            email = user_record['email'],
            user_id = user_record['id'],)
        self.insert(newPilot)