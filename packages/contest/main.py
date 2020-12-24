#!/usr/bin/env python
# encoding: utf-8
from gnr.app.gnrdbo import GnrDboTable, GnrDboPackage

class Package(GnrDboPackage):
    def config_attributes(self):
        return dict(comment='contest package',sqlschema='contest',sqlprefix=True,
                    name_short='Contest', name_long='Contest', name_full='Contest')
                    
    def config_db(self, pkg):
        pass
        
class Table(GnrDboTable):
    pass
