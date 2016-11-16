#!/usr/bin/python

import thread
import time
import requests

# Define a function for the thread
def print_time( threadName, delay):
   count = 0
   while count < 10:
      time.sleep(delay)
      count += 1
      r=requests.get('http://10.30.2.27/client.php')
      print threadName, "|| Count: ", count, r

# Create two threads as follows
try:
   thread.start_new_thread( print_time, ("Thread-1", 1, ) )
   thread.start_new_thread( print_time, ("Thread-2", 1, ) )
   thread.start_new_thread( print_time, ("Thread-3", 2, ) )
   thread.start_new_thread( print_time, ("Thread-4", 1, ) )
   thread.start_new_thread( print_time, ("Thread-5", 2, ) )
except:
   print "Error: unable to start thread"

while 1:
  pass
