#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Import get_credentials metode iz credentials skripte
from credentials import get_credentials
#Import ceilometer klijent
import ceilometerclient.client
#Import klase za vrijeme
import time
#U credentials referencu zapisujemo vrijednosti vracene iz get_credentials() metode iz credentials.py skripte
credentials = get_credentials()
#Stvaramo ceilometerclient objekt pomocu get_client metode i pokazivaca na credentials objekt koji popunjava potrebne postavke za get_client metodu
cclient = ceilometerclient.client.get_client(2, **credentials)

#stvaramo datoteku za zapis metrika
file = open('metrics.txt', 'a')

#vrijednosti id pojedinih instanci
id1 = "97e754fd-8ee8-4543-b3a8-0007ae55db08"
id2 = "46e33cd6-c375-4c8e-a64a-6bfd829dc36f"
id3 = "f98f2521-0a4c-4ef5-88e5-efe40480d0ae"

#podesavamo vrijednosti pocetnog i krajnjeg datuma
hourStart = 13
hourEnd = 17
minuteStart = 00
minuteEnd = 00
year = 2016
month = 12
day = 15
#tsStart = '2016-11-28T13:10:00+01:00'
#tsEnd = '2016-11-28T13:20:00+01:00'

while (hourStart != hourEnd or minuteStart != minuteEnd):

	if minuteStart == 0:
		tsStart = str(year) + '-' + str(month) + '-' + str(day) +'T' + str(hourStart) + ':' + str(minuteStart) + str(minuteStart) + ':00Z'
	else:
		tsStart = str(year) + '-' + str(month) + '-' + str(day) +'T' + str(hourStart) + ':' + str(minuteStart) + ':00Z'

	if minuteStart == 50:
		minuteStart = 0
		hourStart += 1
	else:
		minuteStart += 10

	if minuteStart == 0:
		tsEnd = str(year) + '-' + str(month) + '-' + str(day) +'T' + str(hourStart) + ':' + str(minuteStart) + str(minuteStart) + ':00Z'
	else:
		tsEnd = str(year) + '-' + str(month) + '-' + str(day) +'T' + str(hourStart) + ':' + str(minuteStart) + ':00Z'

	query1 = [dict(field='resource_id', op='eq', value=id1), dict(field='timestamp', op='ge', value=tsStart), dict(field='timestamp', op='le', value=tsEnd)]

	query2 = [dict(field='resource_id', op='eq', value=id2), dict(field='timestamp', op='ge', value=tsStart), dict(field='timestamp', op='le', value=tsEnd)]

	query3 = [dict(field='resource_id', op='eq', value=id3), dict(field='timestamp', op='ge', value=tsStart), dict(field='timestamp', op='le', value=tsEnd)]

	#query3t = [dict(field='resource_id', op='eq', value=id3), dict(field='timestamp', op='ge', value='2016-12-15T15:00:00Z'), dict(field='timestamp', op='le', value='2016-12-15T17:00:00Z')]

#	for sample in cclient.statistics.list(meter_name = 'memory', q = query1):
#		memoryMax1=sample.max
#	for sample in cclient.statistics.list(meter_name = 'memory', q = query2):
#		memoryMax2=sample.max
#	for sample in cclient.statistics.list(meter_name = 'memory', q = query3):
#		memoryMax3=sample.max

#	for sample in cclient.statistics.list(meter_name = 'memory.usage', q = query1):
#		memoryUsageAvg1 = int(sample.avg)
#	for sample in cclient.statistics.list(meter_name = 'memory.usage', q = query2):
#		memoryUsageAvg2 = int(sample.avg)
#	for sample in cclient.statistics.list(meter_name = 'memory.usage', q = query3):
#		memoryUsageAvg3 = int(sample.avg)

#	print cclient.statistics.list(meter_name = 'cpu_util', q = query3t)

#	for sample in cclient.statistics.list(meter_name = 'cpu_util', q = query1):
#		cpuAvg1=sample.avg
#	for sample in cclient.statistics.list(meter_name = 'cpu_util', q = query2):
#		cpuAvg2=sample.avg
#	for sample in cclient.statistics.list(meter_name = 'cpu_util', q = query3):
#		cpuAvg3=sample.avg


	for sample in cclient.statistics.list(meter_name = 'cpu_util', q = query1):
		cpuUtilsAvg1 = sample.max
		cpuUtilsAvg1 = float("{0:.2f}".format(cpuUtilsAvg1))
	for sample in cclient.statistics.list(meter_name = 'cpu_util', q = query2):
		cpuUtilsAvg2 = sample.max
		cpuUtilsAvg2 = float("{0:.2f}".format(cpuUtilsAvg2))
	for sample in cclient.statistics.list(meter_name = 'cpu_util', q = query3):
		cpuUtilsAvg3 = sample.max
		cpuUtilsAvg3 = float("{0:.2f}".format(cpuUtilsAvg3))

	print "\n\n"
	print "Duration start:\t" + tsStart
	print "Duration end:\t" + tsEnd
	print "\n"
	print "CPU"
	print "----"
	print "**************************************************************************"
#	print "Prosječna iskoristenost  - instanca 1:\t\t", cpuAvg1, "%"
#	print "Prosječna iskoristenost  - instanca 2:\t\t", cpuAvg2, "%"
#	print "Prosječna iskoristenost  - instanca 3:\t\t", cpuAvg3, "%"
	print "Maksimalna iskoristenost  - instanca 1:\t\t", cpuUtilsAvg1, "%"
	print "Maksimalna iskoristenost  - instanca 2:\t\t", cpuUtilsAvg2, "%"
	print "Maksimalna iskoristenost  - instanca 3:\t\t", cpuUtilsAvg3, "%"
	print "**************************************************************************"


	stats = tsStart + '\t' + tsEnd + '\t' + str(cpuUtilsAvg1) + '\t' + str(cpuUtilsAvg2) + '\t' + str(cpuUtilsAvg3) + '\n'
#+ str(memoryUsageAvg1) + '\t' + str(memoryUsageAvg2) + '\t' + str(memoryUsageAvg3) + '\n'
	file.write(stats)

file.close()
