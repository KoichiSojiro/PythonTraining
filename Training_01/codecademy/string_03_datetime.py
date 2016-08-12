'''
Created on May 11, 2016

@author: trannh08
'''
from datetime import datetime
now = datetime.now()
print(now)
print ("%s/%s/%s %s:%s:%s" % (now.month, now.day, now.year, now.hour, now.minute, now.second))