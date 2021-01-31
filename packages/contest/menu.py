#!/usr/bin/python3
# -*- coding: utf-8 -*-

def config(root,application=None):
    contest = root.branch('Contest')
    contest.thpage('!![en]Contest Directors',table='contest.contest_director')
    contest.webpage(u"!![en]Managment Mobile",filepath="/f3kp/contest_page")
