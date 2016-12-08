#!/usr/bin/python

import time
import requests
import math
import random
from datetime import datetime

def genTraffic(name, num, k):
	file = open( name + '.txt', 'a')
	count = 0
	while count < num:
		pp = random.expovariate(1/k)
		time.sleep(pp)
		count += 1
		a= datetime.now()
		r=requests.get('http://10.30.2.27/client.php')
		b= datetime.now()
		c= b-a
		print name, "-", count," || Value: ",pp, " Start: ",a, " End: "  ,b," Diff: ",c," || ", r.text,"\n"
		stats = str(c) + ";" + r.text + "\n"
		file.write(stats)
	file.close()

genTraffic("case-1", 260, 5.0)
genTraffic("case-2", 900, 2.0)
genTraffic("case-3", 1440, 0.5)

print "KRAJ GENERIRANJA"
