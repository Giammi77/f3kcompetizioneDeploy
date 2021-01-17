#!/usr/bin/env python
# encoding: utf-8
def config(root,application=None):
    timer = root.branch(u"!![en]Timer")
    timer.thpage(u"!![en]Audio", table="timer.audio")
    timer.thpage(u"!![en]Timer", table="timer.timer")
    timer.lookups(u"!![en]Auxiliar Table", lookup_manager="timer")
    timer.webpage(u"!![en]Timer Setup Importer",filepath="/timer/timer_setup_importer" )
