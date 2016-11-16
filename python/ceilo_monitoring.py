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
query = [dict(field='timestamp', op='gt', value='2016-11-16T12:00:00Z'), dict(field='timestamp', op='lt', value='2016-11-16T15:30:00Z')]
while True:
	#for petlja koja u sample zapisuje list tip podatka koji sadrzi sve podatke o izlaznom bandwithu
	for sample in cclient.statistics.list(meter_name = 'network.outgoing.bytes', q = query):
		#Dodjeljujemo pomocnim varijablama vrijednosti iz liste, tj sample.min
		bwoutmin=sample.min
		bwoutavg=sample.avg
		bwoutmax=sample.max
		bwoutsum=sample.sum
		bwoutcount=sample.count
	for sample in cclient.statistics.list(meter_name = 'network.incoming.bytes', q = query):
		#Dodjeljujemo pomocnim varijablama vrijednosti iz liste, tj sample.min
		bwinmin=sample.min
		bwinavg=sample.avg
		bwinmax=sample.max
		bwinsum=sample.sum
		bwincount=sample.count
	for sample in cclient.statistics.list(meter_name = 'memory', q = query):
		memoryMax=sample.max
	for sample in cclient.statistics.list(meter_name = 'memory.usage', q = query):
		memoryUsageAvg=sample.avg
	for sample in cclient.statistics.list(meter_name = 'cpu', q = query):
		cpuAvg=sample.avg
	for sample in cclient.statistics.list(meter_name = 'cpu_util', q = query):
		cpuUtilsAvg=sample.avg
        for sample in cclient.statistics.list(meter_name = 'vcpus', q = query):
                vcpusAvg=sample.avg

	#bw varijabla sadrzi kumulativni bandwith, tj zbroj incoming i outgoing bandwith-a
	bw = bwoutsum+bwinsum
	print "\n"
	#Print incoming bandwith-a na standardni output
	print "Bandwidth incoming:\t\t", bwinsum, "Count", bwincount
	#Print outgoing bandwith-a na standardni output
	print "Bandwidth outgoing:\t\t", bwoutsum, "Count", bwoutcount
	#Print kumulativnog bandwith-a na standardni output
	print "Bandwidth:\t\t\t" , bw , "Bytes "

	print "Memory allocated:\t\t", memoryMax, "MB"
	print "Memory average usage:\t\t", memoryUsageAvg, "MB"
	print "CPU average time used:\t\t", cpuAvg/1000000000, "s"
	print "CPU average utils:\t\t", cpuUtilsAvg, "%"
	print "VCPUs:\t\t\t\t", vcpusAvg
#	query = [dict(field='timestamp', op='gt', value='2016-11-16T12:00:00Z'), dict(field='timestamp', op='lt', value='2016-11-16T15:30:00Z')]
#        print cclient.statistics.list(meter_name='instance', q = query)

        #sleep komanda pauzira izvodenje na 3 sekunde nakon cega se ponovno izvode dvije for petlje
	time.sleep(3)
