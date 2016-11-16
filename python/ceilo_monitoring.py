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
while True:
	#for petlja koja u sample zapisuje list tip podatka koji sadrzi sve podatke o izlaznom bandwithu
	for sample in cclient.statistics.list('network.outgoing.bytes'):
		#Dodjeljujemo pomocnim varijablama vrijednosti iz liste, tj sample.min
		bwoutmin=sample.min
		bwoutavg=sample.avg
		bwoutmax=sample.max
		bwoutsum=sample.sum
		bwoutcount=sample.count
	for sample in cclient.statistics.list('network.incoming.bytes'):
		#Dodjeljujemo pomocnim varijablama vrijednosti iz liste, tj sample.min
		bwinmin=sample.min
		bwinavg=sample.avg
		bwinmax=sample.max
		bwinsum=sample.sum
		bwincount=sample.count
	for sample in cclient.statistics.list('memory'):
		memoryAvg=sample.avg
	for sample in cclient.statistics.list('memory.usage'):
		memoryUsageAvg=sample.avg
	for sample in cclient.statistics.list('cpu'):
		cpuAvg=sample.avg
	for sample in cclient.statistics.list('cpu_util'):
		cpuUtilsAvg=sample.avg
        for sample in cclient.statistics.list('vcpus'):
                vcpusAvg=sample.avg

	#bw varijabla sadrzi kumulativni bandwith, tj zbroj incoming i outgoing bandwith-a
	bw = bwoutsum+bwinsum
	print "\n"
	#Print incoming bandwith-a na standardni output
	print "Bandwih incoming:\t\t", bwinsum, "Count", bwincount
	#Print outgoing bandwith-a na standardni output
	print "Bandwith outgoing:\t\t", bwoutsum, "Count", bwoutcount
	#Print kumulativnog bandwith-a na standardni output
	print "Bandwith:\t\t\t" , bw , "Bytes "

	print "Memory average in last day:\t", memoryAvg, "MB"
	print "Memory average usage:\t\t", memoryUsageAvg, "MB"
	print "CPU average time used:\t\t", cpuAvg/1000000000, "s"
	print "CPU average utils:\t\t", cpuUtilsAvg, "%"
	print "VCPUs:\t\t\t\t", vcpusAvg


        #sleep komanda pauzira izvodenje na 3 sekunde nakon cega se ponovno izvode dvije for petlje
	time.sleep(3)
