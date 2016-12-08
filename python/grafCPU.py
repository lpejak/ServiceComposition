import matplotlib.pyplot as plt
import math

text1 = open('metrics.txt')
data0 = []
data1 = []
cpu1 = []
cpu2 = []
cpu3 = []

case = "CPUload: "

for line in text1:
	d = line.split('\t')
	x=d[0][10:-4]
	data0.append(x.replace(":","."))
	data1.append(x)
	cpu1.append(d[2])
	cpu2.append(d[3])
	cpu3.append(d[4])

plt.plot(data0, cpu1, 'r')
plt.autoscale(tight=True)
plt.title(case + 'Servis 1')
plt.ylabel('CPU opterecenje (%)')
plt.xlabel('Vrijeme (H.m)')
plt.grid(linestyle='-')
plt.show()

plt.plot(data0, cpu2, 'r')
plt.autoscale(tight=True)
plt.title(case + 'Servis 2')
plt.ylabel('CPU opterecenje (%)')
plt.xlabel('Vrijeme (H.m)')
plt.grid(linestyle='-')
plt.show()

plt.plot(data0, cpu3, 'r')
plt.autoscale(tight=True)
plt.title(case + 'Servis 3')
plt.ylabel('CPU opterecenje (%)')
plt.xlabel('Vrijeme (H.m)')
plt.grid(linestyle='-')
plt.show()
