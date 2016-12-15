#!/usr/bin/python

import time
import thread
import requests
import math
import random
from datetime import datetime



def funkcija(file, count, name, koef):
	r = requests.get('http://localhost/client.php?')
	stats = str(koef) + ";" + r.text + "\n"
	print name, "-", count," || Value: ",stats,"\n"
	file.write(stats)

def genTraffic(name, num, k):
	file = open( name + '.txt', 'a')
	count = 0
	while count < num:
		pp = random.expovariate(1/k)
		time.sleep(pp)
		count += 1
		try:
			thread.start_new_thread(funkcija, (file, count, name, pp))
		except:
			print "ne radi"		
		print name, "-", count," || STARTED\n"
	time.sleep(5)
		

genTraffic("case-1", 1800, 1.0)
genTraffic("case-2", 3600, 0.5)
genTraffic("case-3", 100, 0.1)

print "KRAJ GENERIRANJA"
