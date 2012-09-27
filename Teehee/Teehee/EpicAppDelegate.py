#-*- coding: utf-8 -*-
#
#  TeeheeAppDelegate.py
#  Teehee
#
#  Created by Jonathon Fuller on 9/26/12.
#  Copyright nottooshabby 2012. All rights reserved.
#

from Foundation import *
from AppKit import *

class EpicAppDelegate(NSObject):
    def applicationDidFinishLaunching_(self, sender):
        NSLog("Application did finish launching.")
