# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 12:38:29 2019

@author: amaniamr
"""

    
calendar1 = []
dailyBounds1 = ['9:30', '20:00']
calendar2 = []
dailyBounds2 = ['9:00', '16:30']
duration = 60

def calendarMatching(calendar1, dailyBounds1, calendar2, dailyBounds2, meeting_duration):
    newCalendar1 = makeFullEvent(calendar1,dailyBounds1)
    newCalendar2 = makeFullEvent(calendar2,dailyBounds2)
    
    fullCalendar = merge(newCalendar1,newCalendar2)
    
    print(fullCalendar)
    return getIntervals(fullCalendar,meeting_duration)

def merge(newCalendar1,newCalendar2):
    temp = newCalendar1 + newCalendar2
    
    temp.sort(key = lambda x: x[0])
    
    merged_calendar = [temp.pop(0)]
    
    for event in temp:
        print(event[0],merged_calendar[-1][1])
        if event[0] <= merged_calendar[-1][1]:
            merged_calendar[-1] = [merged_calendar[-1][0],max(event[1],merged_calendar[-1][1])]
        else:
            merged_calendar.append(event)
            
    print(merged_calendar)
    return merged_calendar
        
def getIntervals(full_calendar,duration):
    result = []
    for i in range(1,len(full_calendar)):
        first = full_calendar[i-1]
        second = full_calendar[i]
        
        if second[0] - first[1] >= duration:
            result.append([first[1],second[0]])
            
    result = list(map(lambda x: [minutes_to_time(x[0]),minutes_to_time(x[1])],result))
    print(result)
    
    return result
    
    
def makeFullEvent(calendar,dailyBound):
    newCalendar = []
    if calendar:
        newCalendar = calendar[:]
    newCalendar.insert(0,["00:00",dailyBound[0]])
    newCalendar.append([dailyBound[1],"23:59"])
    newCalendar = list(map(lambda x: [time_to_minutes(x[0]),time_to_minutes(x[1])] , newCalendar))
    return newCalendar

def time_to_minutes(x):
    h,m = x.split(":")
    return int(h) * 60 + int(m)

def minutes_to_time(x):
    h = x // 60
    m = x % 60
    
    time_string = str(h) + ":"+ (str(m) if m > 9 else "0" + str(m))
    return time_string
    


calendarMatching(calendar1,dailyBounds1,calendar2,dailyBounds2,duration)

print(minutes_to_time(1439))