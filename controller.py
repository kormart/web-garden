#!/usr/bin/python

import time
from time import localtime
#import requests

mode = '7'

while 1:
    time.sleep(2)
    time_now = localtime()
    day = time_now.tm_yday
    hour = time_now.tm_hour
    minute = time_now.tm_min
    second = time_now.tm_sec
    string = str(day).zfill(3) + "." + str(hour).zfill(2) + "." + str(minute).zfill(2) + "." + str(second).zfill(2) + ":" 
    print string
    if hour > 18 or hour < 7 :
        night = 1
	day = 0
    else :
	night = 0
	day = 1
    print "Day: ",  day
    print "Night: ",  night

#    try:
#       url = "http://backabo.net:8000/test-page?name=" + string
#       response = requests.get(url)
#       mode = str(response.text)
#    except (requests.ConnectionError) as ex:
#       print "Error: %s" % ex
#    print '%s:%s'%(string, string2)
    time.sleep(58)
   
