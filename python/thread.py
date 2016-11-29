#!/usr/bin/python

import thread
import time
import requests
import math
import random

# Define a function for the thread
def print_time( threadName):
	count = 0
	while count < 100:
		pp = random.expovariate(1/15.0)
		time.sleep(math.ceil(pp))
		if(pp>15.0):
			count += 1
			r=requests.get('http://10.30.2.27/client.php')
			print threadName, " || Count: ", count," || Value: ", pp, r,"\n"

try:
	thread.start_new_thread( print_time, ("User-01", ) )
	thread.start_new_thread( print_time, ("User-02", ) )
	thread.start_new_thread( print_time, ("User-03", ) )
	thread.start_new_thread( print_time, ("User-04", ) )
	thread.start_new_thread( print_time, ("User-05", ) )
	thread.start_new_thread( print_time, ("User-06", ) )
	thread.start_new_thread( print_time, ("User-07", ) )
	thread.start_new_thread( print_time, ("User-08", ) )
	thread.start_new_thread( print_time, ("User-09", ) )
	thread.start_new_thread( print_time, ("User-10", ) )
	thread.start_new_thread( print_time, ("user-11", ) )
	thread.start_new_thread( print_time, ("User-12", ) )
        thread.start_new_thread( print_time, ("User-13", ) )
        thread.start_new_thread( print_time, ("User-14", ) )
        thread.start_new_thread( print_time, ("User-15", ) )
except:
	print "Error: problemi sa dretvama"

while 1:
	pass
