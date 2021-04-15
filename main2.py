import csv
import glob

from statistics import mean
from cmath import rect
from math import radians, acos, cos, sin


class newPhasor:
    def __init__(self, voltageRadialCoordinate=0, currentRadialCoordinate=0, powerFactorAngle=0, angularCoordinate=0):
        self.voltageRadialCoordinate = voltageRadialCoordinate
        self.currentRadialCoordinate = currentRadialCoordinate

        self.powerFactorAngle = powerFactorAngle

        self.voltageAngularCoordinate = angularCoordinate
        self.currentAngularCoordinate = angularCoordinate + self.powerFactorAngle

        self.currentPolar = rect(self.currentRadialCoordinate, radians(angularCoordinate + powerFactorAngle))
        self.voltagePolar = rect(voltageRadialCoordinate, radians(angularCoordinate))

        self.apparentPower = self.voltageRadialCoordinate * self.currentRadialCoordinate
        self.realPower = abs(self.voltageRadialCoordinate * self.currentRadialCoordinate * cos(self.powerFactorAngle))
        self.reactivePower = abs(self.voltageRadialCoordinate * self.currentRadialCoordinate * sin(self.powerFactorAngle))

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


csv_files = glob.glob('data/*.csv')
for csv_file in csv_files:
    temp_list = []
    with open(csv_file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count > 2:
                phaseA = newPhasor(voltageRadialCoordinate=float(row[3]), currentRadialCoordinate=float(row[4]),
                                   powerFactorAngle=acos(float(row[8])),
                                   angularCoordinate=60)
                phaseB = newPhasor(voltageRadialCoordinate=float(row[10]), currentRadialCoordinate=float(row[11]),
                                   powerFactorAngle=acos(float(row[15])),
                                   angularCoordinate=300)
                phaseC = newPhasor(voltageRadialCoordinate=float(row[17]), currentRadialCoordinate=float(row[18]),
                                   powerFactorAngle=acos(float(row[22])),
                                   angularCoordinate=180)

                temp_dic = {"Day":int(row[1].split("/")[1]),"Month":int(row[1].split("/")[0]),"Year":int(row[1].split("/")[2])+2000,
                            "Hour":int(row[2].split(":")[0]), "Minute":int(row[2].split(":")[1]), "Second":int(row[2].split(":")[2]),
                            "Phase A - Voltage (V)":phaseA.voltageRadialCoordinate, "Phase A - Current (A)":phaseA.currentRadialCoordinate,
                            "Phase A - Power Factor (Degrees)":phaseA.currentAngularCoordinate,
                            "Phase A - Apparent Power (VA)":phaseA.apparentPower,
                            "Phase A - Real Power(W)":phaseA.realPower,
                            "Phase A - reactivePower(VAr)": phaseA.reactivePower,

                            "Phase B - Voltage (V)": phaseB.voltageRadialCoordinate,
                            "Phase B - Current (A)": phaseB.currentRadialCoordinate,
                            "Phase B - Power Factor (Degrees)": phaseB.currentAngularCoordinate,
                            "Phase B - Apparent Power (VA)": phaseB.apparentPower,
                            "Phase B - Real Power(W)": phaseB.realPower,
                            "Phase B - reactivePower(VAr)": phaseB.reactivePower,

                            "Phase C - Voltage (V)": phaseC.voltageRadialCoordinate,
                            "Phase C - Current (A)": phaseC.currentRadialCoordinate,
                            "Phase C - Power Factor (Degrees)": phaseC.currentAngularCoordinate,
                            "Phase C - Apparent Power (VA)": phaseC.apparentPower,
                            "Phase C - Real Power(W)": phaseC.realPower,
                            "Phase C - reactivePower(VAr)": phaseC.reactivePower,

                            "System - Voltage (V)": mean([phaseA.voltageRadialCoordinate, phaseB.voltageRadialCoordinate, phaseC.voltageRadialCoordinate]),
                            "System - Current (A)": mean([phaseA.currentRadialCoordinate, phaseB.currentRadialCoordinate, phaseC.currentRadialCoordinate]),
                            "System - Power Factor (Degrees)": mean([phaseA.currentAngularCoordinate, phaseB.currentAngularCoordinate, phaseC.currentAngularCoordinate]),
                            "System - Apparent Power (VA)": sum([phaseA.apparentPower, phaseB.apparentPower, phaseC.apparentPower]),
                            "System - Real Power(W)": sum([phaseA.realPower, phaseB.realPower, phaseC.realPower]),
                            "System - reactivePower(VAr)": sum([phaseA.reactivePower, phaseB.reactivePower, phaseC.reactivePower])
                            }
                temp_list.append(temp_dic)
                line_count = line_count + 1
            else:
                line_count = line_count + 1
    keys = temp_list[0].keys()
    with open(csv_file.name.split("/")[1], 'w', newline='')  as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(temp_list)
