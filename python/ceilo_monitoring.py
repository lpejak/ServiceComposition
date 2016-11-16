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

id1 = '3c420b81-2225-4243-97d4-c27032d4cefb'
id2 = '59456355-77e0-4a4b-9d29-60a92c9cd396'
id3 = '87f6a3d3-f635-4876-bdf3-c39c447466eb'
tsStart = '2016-11-16T12:00:00Z'
tsEnd = '2016-11-16T16:30:00Z'

query1 = [dict(field='resource_id', op='eq', value=id1), dict(field='timestamp', op='gt', value=tsStart), dict(field='timestamp', op='lt', value=tsEnd)]

query2 = [dict(field='resource_id', op='eq', value=id2), dict(field='timestamp', op='gt', value=tsStart), dict(field='timestamp', op='lt', value=tsEnd)]

query3 = [dict(field='resource_id', op='eq', value=id3), dict(field='timestamp', op='gt', value=tsStart), dict(field='timestamp', op='lt', value=tsEnd)]

while True:
	for sample in cclient.statistics.list(meter_name = 'memory', q = query1):
		memoryMax1=sample.max
	for sample in cclient.statistics.list(meter_name = 'memory', q = query2):
		memoryMax2=sample.max
	for sample in cclient.statistics.list(meter_name = 'memory', q = query3):
                memoryMax3=sample.max
	for sample in cclient.statistics.list(meter_name = 'memory.usage', q = query1):
		memoryUsageAvg1=sample.avg
        for sample in cclient.statistics.list(meter_name = 'memory.usage', q = query2):
                memoryUsageAvg2=sample.avg
        for sample in cclient.statistics.list(meter_name = 'memory.usage', q = query3):
                memoryUsageAvg3=sample.avg
	for sample in cclient.statistics.list(meter_name = 'cpu', q = query1):
		cpuAvg1=sample.avg
	for sample in cclient.statistics.list(meter_name = 'cpu_util', q = query1):
		cpuUtilsAvg1=sample.avg
        for sample in cclient.statistics.list(meter_name = 'vcpus', q = query1):
                vcpusAvg1=sample.avg
        for sample in cclient.statistics.list(meter_name = 'cpu', q = query2):
                cpuAvg2=sample.avg
        for sample in cclient.statistics.list(meter_name = 'cpu_util', q = query2):
                cpuUtilsAvg2=sample.avg
        for sample in cclient.statistics.list(meter_name = 'vcpus', q = query2):
                vcpusAvg2=sample.avg
        for sample in cclient.statistics.list(meter_name = 'cpu', q = query3):
                cpuAvg3=sample.avg
        for sample in cclient.statistics.list(meter_name = 'cpu_util', q = query3):
                cpuUtilsAvg3=sample.avg
        for sample in cclient.statistics.list(meter_name = 'vcpus', q = query3):
                vcpusAvg3=sample.avg
	for sample in cclient.statistics.list(meter_name = 'disk.allocation', q = query1):
                diskAloc1=sample.avg
        for sample in cclient.statistics.list(meter_name = 'disk.allocation', q = query2):
                diskAloc2=sample.avg
        for sample in cclient.statistics.list(meter_name = 'disk.allocation', q = query3):
                diskAloc3=sample.avg


	print "\n"
	print "CPU"
	print "----"
        print "**************************************************************************"
        print "Prosjecno vrijeme iskoristeno - instanca 1:\t\t", cpuAvg1/1000000000, "s"
        print "Prosjecna iskoristenost  - instanca 1:\t\t\t", cpuUtilsAvg1, "%"
        print "Prosjecno vrijeme iskoristeno - instanca 2:\t\t", cpuAvg2/1000000000, "s"
        print "Prosjecna iskoristenost  - instanca 2:\t\t\t", cpuUtilsAvg2, "%"
        print "Prosjecno vrijeme iskoristeno - instanca 3:\t\t", cpuAvg3/1000000000, "s"
        print "Prosjecna iskoristenost  - instanca 3:\t\t\t", cpuUtilsAvg3, "%"
	print "**************************************************************************"

	print "\n"
	print "MEMORIJA"
        print "---------"
        print "**************************************************************************"
	print "Alocirano - instanca 1:\t\t\t\t", memoryMax1, "MB"
        print "Alocirano - instanca 2:\t\t\t\t", memoryMax2, "MB"
        print "Alocirano - instanca 3:\t\t\t\t", memoryMax3, "MB"
	print "Prosjecna iskoristenost - instanca 1:\t\t", memoryUsageAvg1, "MB"
        print "Prosjecna iskoristenost - instanca 2:\t\t", memoryUsageAvg2, "MB"
        print "Prosjecna iskoristenost - instanca 3:\t\t", memoryUsageAvg3, "MB"
	print "**************************************************************************"

	print "\n"
	print "DISK"
        print "-----"
        print "**************************************************************************"
	print "Disk alocation instanca 1:\t\t", diskAloc1/1000000, "MB"
	print "Disk alocation instanca 2:\t\t", diskAloc2/1000000, "MB"
	print "Disk alocation instanca 3:\t\t", diskAloc3/1000000, "MB"
        print "**************************************************************************"

#	cpu_util_sample = cclient.samples.list('cpu_util')
#	for each in cpu_util_sample:
#		print each.timestamp, each.resource_id, each.counter_volume
        #sleep komanda pauzira izvodenje na 3 sekunde nakon cega se ponovno izvode dvije for petlje
	time.sleep(3)
