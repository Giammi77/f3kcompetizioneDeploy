#!/usr/bin/env python
# encoding: utf-8
from gnr.app.gnrdbo import GnrDboTable, GnrDboPackage

class Package(GnrDboPackage):
    def config_attributes(self):
        return dict(comment='TIMER package',sqlschema='timer',sqlprefix=True,
                    name_short='Timer', name_long='Timer', name_full='Timer')
                    
    def config_db(self, pkg):
        pass
        
class Table(GnrDboTable):
    pass
