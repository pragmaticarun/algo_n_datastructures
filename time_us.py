# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 09:50:14 2019

@author: amaniamr
"""

import datetime

t = datetime.datetime.now()

class CallMonitor:
    def __init__(self):
        self.callList = []
        
    def addCall(self,start,end):
        #TODO validate start and end are valid timestamps
        if start > end:
            raise ValueError("Start time is greater than end time")
            
        self.callList.append((start,end))
        
    def queryActiveCall(self,start,end):
        if start > end:
            raise ValueError("Start time is greater than end time")
        
        numActiveCalls = 0
        for s,e in self.callList:
            if start < e and end >= e:
                numActiveCalls += 1     
        return numActiveCalls


cm = CallMonitor()

cm.addCall(0,1)
cm.addCall(0,10)
cm.addCall(2,3)
cm.addCall(2,3)
cm.addCall(1,5)
cm.addCall(8,11)
cm.addCall(1,1)

print(cm.queryActiveCall(0,2))
cm.addCall(0,1)
print(cm.queryActiveCall(0,2))
        
        