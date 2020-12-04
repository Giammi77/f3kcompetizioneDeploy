#!/usr/bin/env python
# encoding: utf-8
from gnr.app.gnrdbo import GnrDboTable, GnrDboPackage

class Package(GnrDboPackage):
    def config_attributes(self):
        return dict(comment='f3kp package',sqlschema='f3kp',sqlprefix=True,
                    name_short='F3kp', name_long='F3kp', name_full='F3kp')
                    
    def config_db(self, pkg):
        pass

    def custom_type_score(self):
        return dict(dtype='N',format='##,###.00')

class Table(GnrDboTable):
    pass
