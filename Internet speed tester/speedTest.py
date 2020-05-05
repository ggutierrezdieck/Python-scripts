# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 11:28:00 2020

@author: Gerardo
"""
import speedtest
from datetime import datetime

class speedTest(object):
    
    def __init__(self):
        self.speeds = {}
        self.speeds['d'] =  {}
        self.speeds['u'] =  {}
        self.speeds['p'] = {}
 
    def __str__(self):
        #TODO: print latest speed
        return str(self.speeds)
    
    def test(self):
        t  = str(datetime.now().strftime("%H:%M"))
        try:
            s = speedtest.Speedtest()
            s.get_servers()
            s.get_best_server()
            s.download()
            s.upload()
        except:
            print("Error trying to test internet")
        else:
            res = s.results.dict()
            self.speeds['d'][t] = round(res["download"] / 1024 / 1024, 2)
            self.speeds['u'][t] = round(res["upload"] / 1024  / 1024, 2)
            self.speeds['p'][t] = res["ping"]
    
    def getLastResult(self):
        return str(self.res['d'][-1] + ',' + self.res['u'][-1]+ ',' + self.res['p'][-1])

    