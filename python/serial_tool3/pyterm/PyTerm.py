#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# generated by wxGlade 0.4.1 on Mon Aug 28 16:52:16 2006

#-------------------------------------------------------------------------------
# Name:        pyterm.PyTerm
# Purpose:     wxApplication for running pyTerm.
#
# Original
# Authors:      Thomas Pani
#
# History:
#   None (at the moment).
#
# Created:     28-August-2006
# Copyright:   (c) 2006 by Thomas Pani
# Licence:     MIT
#-------------------------------------------------------------------------------


import wx

from pyterm.MainFrame import MainFrame

try:
    import psyco
    psyco.full()
except ImportError:
    print 'Psyco not installed, the program will just run slower'


class PyTerm(wx.App):
    def OnInit(self):
        wx.InitAllImageHandlers()
        main_frame = MainFrame(None, -1, "")
        self.SetTopWindow(main_frame)
        main_frame.Show()
        return 1

# end of class PyTerm

if __name__ == "__main__":
    PyTerm = PyTerm(0)
    PyTerm.MainLoop()
