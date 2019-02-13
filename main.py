#Imports from Standard Python Libraries
from json import loads, dumps
from math import radians, degrees
from cmath import rect, polar

import numpy as np
import matplotlib.pyplot as plt

#Import from Custom Python Libraries


#Define an new class to hold Phasers
def creatReactents(polarA,polarB):
	return 0



def mapRange(x, from_min, from_max, to_min, to_max):
    return (x - from_min) * (to_max - to_min) / (from_max - from_min) + to_min


def graph_p3_w4(phase_a, phase_b, phase_c, scale_voltage = 1, scale_current = 1):
	fig = plt.figure()
	ax = fig.add_subplot(111, polar=True)
	ax.set_rmax(5.05)
	graphMarkers = np.array(
		[r'$E_{NC}$', r'$E_{AC}$', r'$E_{AN}$', r'$E_{AB}$', r'$E_{NB}$', r'$E_{CB}$', r'$E_{CN}$', r'$E_{CA}$',
		 r'$E_{NA}$', r'$E_{BA}$', r'$E_{BN}$', r'$E_{BC}$'])
	plt.xticks(
		[0, 0.523598776, 1.047197551, 1.570796327, 2.094395102, 2.617993878, 3.141592654, 3.665191429, 4.188790205,
		 4.71238898, 5.235987756, 5.759586532], graphMarkers)
	ax.set_rgrids([], angle=345.)
	fig.set_size_inches(8, 8, forward=False)
	dictForLegend = [plt.polar([0, 0], [0, 0], marker='p', color='black', label='Current Element'),
					 plt.polar([0, 0], [0, 0], marker='*', color='black', label='Voltage Element'),
					 plt.polar([0, 0], [0, 0], marker=' ', color='black', linestyle='--',
							   label='Sum of Currents')]
	plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), shadow=True, ncol=3)
	#                      A Phase                      #
	x = polar(phase_a.returnVoltagePolar() * scale_voltage)
	plt.polar([0, x[1]], [0, x[0]], marker='p', color='red')
	ax.annotate(r'$E_{AN}$', xy=(x[1], x[0]), xytext=(10, 0), textcoords='offset points', ha='center', va='bottom')
	x = polar(phase_a.returnCurrentPolar() * scale_current)
	plt.polar([0, x[1]], [0, x[0]], marker='*', color='firebrick')
	ax.annotate(r'$I_{A}$', xy=(x[1], x[0]), xytext=(10, 0), textcoords='offset points',
				ha='center', va='bottom')
	#                      B Phase                      #
	x = polar(phase_b.returnVoltagePolar() * scale_voltage)
	plt.polar([0, (x[1])], [0, x[0]], marker='p', color='yellow')
	ax.annotate(r'$E_{AN}$', xy=(x[1], x[0]), xytext=(10, 0), textcoords='offset points', ha='center', va='bottom')
	x = polar(phase_b.returnCurrentPolar() * scale_current)
	plt.polar([0, x[1]], [0, x[0]], marker='*', color='gold')
	ax.annotate(r'$I_{B}$', xy=(x[1], x[0]), xytext=(10, 0), textcoords='offset points',
				ha='center', va='bottom')

	#                      C Phase                      #
	x = polar(phase_c.returnVoltagePolar() * scale_voltage)
	plt.polar([0, x[1]], [0, x[0]], marker='p', color='blue')
	ax.annotate(r'$E_{CN}$', xy=(x[1], x[0]), xytext=(10, 0), textcoords='offset points', ha='center', va='bottom')

	x = polar(phase_c.returnCurrentPolar() * scale_current)
	plt.polar([0, x[1]], [0, x[0]], marker='*', color='navy')
	ax.annotate(r'$I_{C}$', xy=(x[1], x[0]), xytext=(10, 0), textcoords='offset points',
				ha='center', va='bottom')
	plt.show()


def graph_p3_w3(phase_a, phase_b, phase_c, scale_voltage=1, scale_current=1):
	fig = plt.figure()
	ax = fig.add_subplot(111, polar=True)
	ax.set_rmax(5.05)
	graphMarkers = np.array(
		[r'$E_{NC}$', r'$E_{AC}$', r'$E_{AN}$', r'$E_{AB}$', r'$E_{NB}$', r'$E_{CB}$', r'$E_{CN}$', r'$E_{CA}$',
		 r'$E_{NA}$', r'$E_{BA}$', r'$E_{BN}$', r'$E_{BC}$'])
	plt.xticks(
		[0, 0.523598776, 1.047197551, 1.570796327, 2.094395102, 2.617993878, 3.141592654, 3.665191429, 4.188790205,
		 4.71238898, 5.235987756, 5.759586532], graphMarkers)
	ax.set_rgrids([], angle=345.)
	fig.set_size_inches(8, 8, forward=False)
	dictForLegend = [plt.polar([0, 0], [0, 0], marker='p', color='black', label='Current Element'),
					 plt.polar([0, 0], [0, 0], marker='*', color='black', label='Voltage Element'),
					 plt.polar([0, 0], [0, 0], marker=' ', color='black', linestyle='--',
							   label='Sum of Currents')]
	plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), shadow=True, ncol=3)
	#                      A Phase                      #
	x = polar(phase_a.returnVoltagePolar() * scale_voltage)
	plt.polar([0, x[1]], [0, x[0]], marker='p', color='red')
	ax.annotate(r'$E_{AN}$', xy=(x[1], x[0]), xytext=(10, 0), textcoords='offset points', ha='center', va='bottom')
	x = polar(phase_a.returnCurrentPolar() * scale_current)
	plt.polar([0, x[1]], [0, x[0]], marker='*', color='firebrick')
	ax.annotate(r'$I_{A}$', xy=(x[1], x[0]), xytext=(10, 0), textcoords='offset points',
				ha='center', va='bottom')
	#                      C Phase                      #
	x = polar(phase_c.returnVoltagePolar() * scale_voltage)
	plt.polar([0, x[1]], [0, x[0]], marker='p', color='blue')
	ax.annotate(r'$E_{CN}$', xy=(x[1], x[0]), xytext=(10, 0), textcoords='offset points', ha='center', va='bottom')

	x = polar(phase_c.returnCurrentPolar() * scale_current)
	plt.polar([0, x[1]], [0, x[0]], marker='*', color='navy')
	ax.annotate(r'$I_{C}$', xy=(x[1], x[0]), xytext=(10, 0), textcoords='offset points',
				ha='center', va='bottom')


	#                      B Phase                      #
	a = polar(phase_a.returnCurrentPolar() * scale_current)
	b = polar(-1 * phase_b.returnCurrentPolar() * scale_current)
	c = polar(phase_c.returnCurrentPolar() * scale_current)
	print("A:",a)
	print("B:",b)
	print("C:",c)
	plt.polar([0, b[1]], [0, b[0]], marker='*', color='gold')
	ax.annotate(r'$I_{B}$', xy=(b[1], b[0]), xytext=(10, 0), textcoords='offset points',
				ha='center', va='bottom')

	ab = polar(rect(a[0],a[1]) + rect(b[0],b[1]))
	print("ab:",ab)
	plt.polar([0, ab[1]], [0, ab[0]], marker='*', color='firebrick', linestyle="--", dashes=(10, 1))
	plt.polar([0, ab[1]], [0, ab[0]], marker='*', color='gold', linestyle="--", dashes=(5, 4))
	ax.annotate(r'$I_{AB}$', xy=(ab[1], ab[0]), xytext=(10, 0), textcoords='offset points',
				ha='center', va='bottom')
	plt.polar([b[1], ab[1]], [b[0], ab[0]], marker='p', color='firebrick',alpha=0.3)
	plt.polar([a[1], ab[1]], [a[0], ab[0]], marker='p', color='gold',alpha=0.6)

	cb = polar(rect(c[0],c[1]) + rect(b[0],b[1]))
	print("cb:",cb)
	plt.polar([0, cb[1]], [0, cb[0]], marker='*', color='blue', linestyle="--", dashes=(10, 1))
	plt.polar([0, cb[1]], [0, cb[0]], marker='*', color='gold', linestyle="-", dashes=(5, 4))
	ax.annotate(r'$I_{AC}$', xy=(cb[1], cb[0]), xytext=(10, 0), textcoords='offset points',
				ha='center', va='bottom')
	plt.polar([b[1], cb[1]], [b[0], cb[0]], marker='p', color='blue',alpha=0.3)
	plt.polar([c[1], cb[1]], [c[0], cb[0]], marker='p', color='gold',alpha=0.6)
	plt.show()


def cross_phase_p3_w4(phase_a, phase_b, phase_c, ct_primary=1, ct_secondary=1, pt_primary=1, pt_secondary=1):
	text_file = open("Cross Phase 3 Phase 4 Wire.csv", "w")
	string_x = str("," , " Phase A" , "," , "Phase B" , "," , "Phase C" , ",")
	text_file.write(string_x)
	string_x = "Multimeter Secondary Voltage (V)" , "," , phase_a.returnVoltageRadialCoordinate()),"," ,phase_b.returnVoltageRadialCoordinate(), "," , phase_c.returnVoltageRadialCoordinate(),","
	text_file.write(str(string_x))

	text_file.close()

class newPhasor:
	def __init__(self, voltageRadialCoordinate = 0, currentRadialCoordinate=0, powerFactorAngle=0, angularCoordinate=0):
		self.voltageRadialCoordinate = voltageRadialCoordinate
		self.currentRadialCoordinate = currentRadialCoordinate
		
		self.powerFactorAngle = powerFactorAngle
		
		self.voltageAngularCoordinate = angularCoordinate
		self.currentAngularCoordinate = angularCoordinate + self.powerFactorAngle
		
		self.currentPolar = rect(self.currentRadialCoordinate, radians(angularCoordinate + powerFactorAngle))
		self.voltagePolar = rect(voltageRadialCoordinate, radians(angularCoordinate))

	def returnVoltageRadialCoordinate(self):
		return self.voltageRadialCoordinate
		
	def returnCurrentRadialCoordinate(self):
		return self.currentRadialCoordinate
		
	def returnPowerFactor(self):
		return self.powerFactor
		
	def returnVoltageAngularCoordinate(self):
		return self.voltageAngularCoordinate
	
	def returnCurrentAngularCoordinate(self):
		return self.currentAngularCoordinate
	
	def returnCurrentPolar(self):
		return self.currentPolar
	
	def returnVoltagePolar(self):
		return self.voltagePolar
		

#Define Phaser Characteristics
phaseA = newPhasor(voltageRadialCoordinate=120,currentRadialCoordinate=16,powerFactorAngle=30,angularCoordinate=60)
phaseB = newPhasor(voltageRadialCoordinate=120,currentRadialCoordinate=5,powerFactorAngle=18,angularCoordinate=300)
phaseC = newPhasor(voltageRadialCoordinate=120,currentRadialCoordinate=12,powerFactorAngle=27,angularCoordinate=180)


graph_p3_w4(phaseA,phaseB,phaseC,1,5)
graph_p3_w3(phaseA,phaseB,phaseC,1,5)
cross_phase_p3_w4(phaseA,phaseB,phaseC)

#where stuff gets done to the data
print(phaseA.returnVoltageRadialCoordinate(), polar(phaseA.returnCurrentPolar())[0], degrees(polar(phaseA.returnCurrentPolar())[1]))
print(phaseB.returnVoltageRadialCoordinate(), polar(phaseB.returnCurrentPolar())[0], degrees(polar(phaseB.returnCurrentPolar())[1]))
print(phaseC.returnVoltageRadialCoordinate(), polar(phaseC.returnCurrentPolar())[0], degrees(polar(phaseC.returnCurrentPolar())[1]))