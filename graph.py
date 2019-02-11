from meterTool import threePhaseTwoWire, threePhaseFourWire
import math
import cmath


rectangularVolts_A = cmath.rect(120, math.radians(0+60))
rectangularCurrent_A = cmath.rect(10, math.radians(25+60))

rectangularVolts_B = cmath.rect(120, math.radians(0+300))
rectangularCurrent_B = cmath.rect(10, math.radians(36+300))

rectangularVolts_C = cmath.rect(120, math.radians(0+180))
rectangularCurrent_C = cmath.rect(10, math.radians(20+180))

threePhaseTwoWire.ThreePhase_TwoWire.create_cross_phasing(rectangularVolts_A=rectangularVolts_A,
                                                          rectangularCurrent_A=rectangularCurrent_A,
                                                          rectangularCurrent_B=rectangularCurrent_B,
                                                          rectangularVolts_C=rectangularVolts_C,
                                                          rectangularCurrent_C=rectangularCurrent_C)
threePhaseTwoWire.ThreePhase_TwoWire.create_graph(rectangularVolts_A=rectangularVolts_A,
                                                          rectangularCurrent_A=rectangularCurrent_A,
                                                          rectangularCurrent_B=rectangularCurrent_B,
                                                          rectangularVolts_C=rectangularVolts_C,
                                                          rectangularCurrent_C=rectangularCurrent_C, curent_scale=1,voltage_sclae=1)
threePhaseFourWire.ThreePhase_FourWire.create_graph(rectangularVolts_A=rectangularVolts_A,
                                                          rectangularCurrent_A=rectangularCurrent_A,
                                                          rectangularVolts_B=rectangularVolts_B,
                                                          rectangularCurrent_B=rectangularCurrent_B,
                                                          rectangularVolts_C=rectangularVolts_C,
                                                          rectangularCurrent_C=rectangularCurrent_C, curent_scale=1,voltage_sclae=1)
