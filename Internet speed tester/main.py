# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 19:40:08 2020

@author: Gerardo
"""

import speedTest
#from threading import Thread
import threading
import time
from datetime import datetime

timeInMin = 1
sleepTime = timeInMin * 60


st = speedTest.speedTest()
 
while True:
  
    st.test()
    print(st)
    print(st.getLastResult)
    
    #t = threading.Thread(target = testSpeed)
    #t.start()

    time.sleep(sleepTime)
    