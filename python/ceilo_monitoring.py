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

#uzimamo vrijednosti id pojedinih instanci
id1 = '3c420b81-2225-4243-97d4-c27032d4cefb'
id2 = '59456355-77e0-4a4b-9d29-60a92c9cd396'
id3 = '87f6a3d3-f635-4876-bdf3-c39c447466eb'

#podesavamo vrijednosti pocetnog i krajnjeg datuma
hourStart = 13
hourEnd = 16
minuteStart = 0
minuteEnd = 0
year = 2016
month = 11
day = 28
#tsStart = '2016-11-28T13:10:00+01:00'
#tsEnd = '2016-11-28T13:20:00+01:00'

while (hourStart != hourEnd or minuteStart != minuteEnd):

	if minuteStart == 0:
		tsStart = str(year) + '-' + str(month) + '-' + str(day) +'T' + str(hourStart) + ':' + str(minuteStart) + str(minuteStart) + ':00+01:00'
	else:
		tsStart = str(year) + '-' + str(month) + '-' + str(day) +'T' + str(hourStart) + ':' + str(minuteStart) + ':00+01:00'

	if minuteStart == 50:
		minuteStart = 0
		hourStart += 1
	else:
		minuteStart += 10

	if minuteStart == 0:
		tsEnd = str(year) + '-' + str(month) + '-' + str(day) +'T' + str(hourStart) + ':' + str(minuteStart) + str(minuteStart) + ':00+01:00'
	else:
		tsEnd = str(year) + '-' + str(month) + '-' + str(day) +'T' + str(hourStart) + ':' + str(minuteStart) + ':00+01:00'

	query1 = [dict(field='resource_id', op='eq', value=id1), dict(field='timestamp', op='ge', value=tsStart), dict(field='timestamp', op='le', value=tsEnd)]

	query2 = [dict(field='resource_id', op='eq', value=id2), dict(field='timestamp', op='ge', value=tsStart), dict(field='timestamp', op='le', value=tsEnd)]

	query3 = [dict(field='resource_id', op='eq', value=id3), dict(field='timestamp', op='ge', value=tsStart), dict(field='timestamp', op='le', value=tsEnd)]

#	for sample in cclient.statistics.list(meter_name = 'memory', q = query1):
#		memoryMax1=sample.max
#	for sample in cclient.statistics.list(meter_name = 'memory', q = query2):
#		memoryMax2=sample.max
#	for sample in cclient.statistics.list(meter_name = 'memory', q = query3):
#		memoryMax3=sample.max

	for sample in cclient.statistics.list(meter_name = 'memory.usage', q = query1):
		memoryUsageAvg1 = int(sample.max)
	for sample in cclient.statistics.list(meter_name = 'memory.usage', q = query2):
		memoryUsageAvg2 = int(sample.max)
	for sample in cclient.statistics.list(meter_name = 'memory.usage', q = query3):
		memoryUsageAvg3 = int(sample.max)

#	for sample in cclient.statistics.list(meter_name = 'cpu', q = query1):
#		cpuAvg1=sample.avg
#	for sample in cclient.statistics.list(meter_name = 'cpu', q = query2):
#		cpuAvg2=sample.avg
#	for sample in cclient.statistics.list(meter_name = 'cpu', q = query3):
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
#	print "Prosjecno vrijeme iskoristeno - instanca 1:\t\t", cpuAvg1/1000000000, "s"
	print "Maksimalna iskoristenost  - instanca 1:\t\t", cpuUtilsAvg1, "%"
#	print "Prosjecno vrijeme iskoristeno - instanca 2:\t\t", cpuAvg2/1000000000, "s"
	print "Maksimalna iskoristenost  - instanca 2:\t\t", cpuUtilsAvg2, "%"
#	print "Prosjecno vrijeme iskoristeno - instanca 3:\t\t", cpuAvg3/1000000000, "s"
	print "Maksimalna iskoristenost  - instanca 3:\t\t", cpuUtilsAvg3, "%"
	print "**************************************************************************"

	print "\n"
	print "MEMORIJA"
	print "---------"
	print "**************************************************************************"
#	print "Alocirano - instanca 1:\t\t\t\t", memoryMax1, "MB"
#	print "Alocirano - instanca 2:\t\t\t\t", memoryMax2, "MB"
#	print "Alocirano - instanca 3:\t\t\t\t", memoryMax3, "MB"
	print "Maksimalna iskoristenost - instanca 1:\t\t", memoryUsageAvg1, "MB"
	print "Maksimalna iskoristenost - instanca 2:\t\t", memoryUsageAvg2, "MB"
	print "Maksimalna iskoristenost - instanca 3:\t\t", memoryUsageAvg3, "MB"
	print "**************************************************************************"

	stats = tsStart + '\t' + tsEnd + '\t' + str(cpuUtilsAvg1) + '\t' + str(cpuUtilsAvg2) + '\t' + str(cpuUtilsAvg3) + '\t' + str(memoryUsageAvg1) + '\t' + str(memoryUsageAvg2) + '\t' + str(memoryUsageAvg3) + '\n'
	file.write(stats)

file.close()


