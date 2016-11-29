#!/usr/bin/python

import thread
import time
import requests

# Define a function for the thread
def print_time( threadName, delay, num):
	count = 0
	while count < num:
		time.sleep(delay)
		count += 1
		r=requests.get('http://10.30.2.27/client.php')
		print threadName, "|| Count: ", count, r


try:
	thread.start_new_thread( print_time, ("User-X", 10, 360, ) )
	thread.start_new_thread( print_time, ("User-Y", 20, 180, ) )
	thread.start_new_thread( print_time, ("User-Z", 30, 120, ) )
	thread.start_new_thread( print_time, ("User-1", 60, 60, ) )
	thread.start_new_thread( print_time, ("User-2", 120, 30, ) )
	thread.start_new_thread( print_time, ("User-3", 180, 20, ) )
	thread.start_new_thread( print_time, ("User-4", 240, 15, ) )
	thread.start_new_thread( print_time, ("user-5", 5*60, 12, ) )
	thread.start_new_thread( print_time, ("User-6", 6*60, 10, ) )
        thread.start_new_thread( print_time, ("User-7", 10*60, 4, ) )
        thread.start_new_thread( print_time, ("User-8", 15*60, 2, ) )
        thread.start_new_thread( print_time, ("User-9", 20*60, 1, ) )
        thread.start_new_thread( print_time, ("User-10", 20*60, 1, ) )
except:
	print "Error: problemi sa dretvama"

while 1:
	pass
