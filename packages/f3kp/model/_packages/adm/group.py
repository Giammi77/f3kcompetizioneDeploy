# encoding: utf-8
from gnr.core.gnrdecorator import metadata
class Table(object):
    # def creaGruppoPilot(self):
    #     if self.checkDuplicate(code='PILOT'):
    #         return
    #     negwroup = self.newrecord(code = 'PILOT',description='Pilot',root_page='/f3kp/pilot_page')
    #     self.insert(negwroup)
    # @metadata(mandatory=True)
    def sysRecord_PILOT(self):
        return self.newrecord(code='PILOT',
                            description='Pilot',
                            rootpage='/f3kp/pilot_page')