#!/usr/bin/env python
# encoding: utf-8
def config(root,application=None):
    f3k = root.branch(u"F3k")
    f3k.thpage(u"!![en]Competition", table="f3kp.competition",formResource='Form',viewResource='View')
    f3k.thpage(u"!![en]Pilot", table="f3kp.pilot")
    f3k.thpage(u"!![en]Registration", table='f3kp.registration')
    f3k.thpage(u"!![en]Competition Task", table='f3kp.competition_task')
    f3k.thpage(u"!![en]Combination",table='f3kp.combination',formResource='FormCombination',viewResource='View_from_pilot')
    f3k.thpage(u"!![en]Flight Time",table='f3kp.flight_time')
    f3k.lookups(u"!![en] Auxiliar Table", lookup_manager="f3kp")
    contest_director = root.branch(u"!![en]Contest Director", pkg='contest')

    dev = root.branch('Developer', tags='admin')
    dev.packageBranch("System", pkg='sys', tags="admin")
    dev.packageBranch("Admin", pkg='adm', tags="admin")
    dev.packageBranch("Email", pkg='email', tags="admin")          
    dev.packageBranch("Docu", pkg='docu', tags="admin")
