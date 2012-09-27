#-*- coding: utf-8 -*-
#
#  main.py
#  Teehee
#
#  Created by Jonathon Fuller on 9/26/12.
#  Copyright nottooshabby 2012. All rights reserved.
#

#import modules required by application
import objc
import Foundation
import AppKit

from PyObjCTools import AppHelper

# import modules containing classes required to start application and load MainMenu.nib
import EpicAppDelegate

# pass control to AppKit
AppHelper.runEventLoop()
