#!/usr/bin/python

import time
import requests
import math
import random
from datetime import datetime

def genTraffic( name):
	count = 0
	while count < 60:
		pp = random.expovariate(1/0.5)
		time.sleep(pp)
		count += 1
		a= datetime.now()
		r=requests.get('http://10.30.2.27/client.php')
		b= datetime.now()
		c= b-a
		print name, "-", count," || Value: ",pp, " Start: ",a, " End: "  ,b," Diff: ",c," || ", r,"\n"

genTraffic("User")
