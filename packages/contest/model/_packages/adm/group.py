# encoding: utf-8

from gnr.core.gnrdecorator import metadata

class Table(object):

    @metadata(mandatory=True)  
    def sysRecord_CDI(self):
        return self.newrecord(description='Contest Director',
                              code='CDI')
