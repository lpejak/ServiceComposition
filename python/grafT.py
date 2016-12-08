import matplotlib.pyplot as plt
import math

text1 = open('response-3.txt')
data0 = []
data1 = []
data2 = []
data3 = []

case = "Case 3: "

for line in text1:
	d = line.split(';')
	data0.append(d[0][6:])
	data1.append(d[1])
	data2.append(d[2])
	data3.append(d[3])

num = len(data0)

plt.plot(data0)
plt.title(case + 'Kompozicija servisa')
plt.ylabel('Vrijeme odziva (s)')
plt.xlabel('Broj zahtjeva')
plt.xlim([0,num])
plt.show()

plt.plot(data1)
plt.title(case + 'Servis 1')
plt.ylabel('Vrijeme odziva (s)')
plt.xlabel('Broj zahtjeva')
plt.xlim([0,num])
plt.show()

plt.plot(data2)
plt.title(case + 'Servis 2')
plt.ylabel('Vrijeme odziva (s)')
plt.xlabel('Broj zahtjeva')
plt.xlim([0,num])
plt.show()

plt.plot(data3)
plt.title(case + 'Servis 3')
plt.ylabel('Vrijeme odziva (s)')
plt.xlabel('Broj zahtjeva')
plt.xlim([0,num])
plt.show()
