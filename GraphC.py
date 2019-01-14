import math
import cmath

import numpy as np
import matplotlib.pyplot as plt

def mapRange (x, from_min, from_max, to_min, to_max):
    return (x - from_min) * (to_max - to_min) / (from_max - from_min) + to_min

#creates the plot for the polar graph
fig = plt.figure()
ax = fig.add_subplot(111, polar=True)
ax.set_rmax(5.05)
z = np.array([r'$E_{NC}$', r'$E_{AC}$', r'$E_{AN}$',
                    r'$E_{AB}$',  r'$E_{NB}$', r'$E_{CB}$',
                    r'$E_{CN}$', r'$E_{CA}$', r'$E_{NA}$',
                    r'$E_{BA}$', r'$E_{BN}$',  r'$E_{BC}$'])
plt.xticks([0,0.523598776,1.047197551,1.570796327,2.094395102,
            2.617993878,3.141592654,3.665191429,4.188790205,
            4.71238898,5.235987756,5.759586532], z)
ax.set_rgrids([], angle=345.)
fig.set_size_inches(8, 8, forward=False)


#                      A Phase                      #
rectangularVolts_A = cmath.rect(120, math.radians(0+60))
rectangularCurrent_A = cmath.rect(5, math.radians(0+60))

x = cmath.polar(rectangularVolts_A)
plt.polar([0,(x[1])],[0,x[0]],marker='p',color='red')
ax.annotate(r'$E_{AN}$', xy=(x[1], x[0]), xytext=(10,0),
            textcoords='offset points', ha='center', va='bottom')

#                      B Phase                      #
rectangularVolts_B = cmath.rect(0, math.radians(0+300))
rectangularCurrent_B = cmath.rect(5, math.radians(0+120))

x = cmath.polar(rectangularVolts_B)
plt.polar([0,(x[1])],[0,x[0]],marker='p',color='yellow')
#ax.annotate(r'$E_{AN}$', xy=(x[1], x[0]), xytext=(10,0),
#            textcoords='offset points', ha='center', va='bottom')


#                      C Phase                      #
rectangularVolts_C = cmath.rect(120, math.radians(0+180))
rectangularCurrent_C = cmath.rect(5, math.radians(0+180))

x = cmath.polar(rectangularVolts_C)
plt.polar([0,(x[1])],[0,x[0]],marker='p',color='blue')
ax.annotate(r'$E_{CN}$', xy=(x[1], x[0]), xytext=(10,0),
            textcoords='offset points', ha='center', va='bottom')

#                      AB Phase                      #
rectangularCurrent_AB = rectangularCurrent_A + rectangularCurrent_B
x = cmath.polar(rectangularCurrent_AB)
plt.polar([0,(x[1])],[0,mapRange(x[0],0,20,0,125)],marker='*',color='gold',linestyle = '-')
plt.polar([0,(x[1])],[0,mapRange(x[0],0,20,0,125)],marker=' ',color='firebrick',linestyle = '--')
ax.annotate(r'$I_{AB}$', xy=(x[1], mapRange(x[0],0,20,0,125)), xytext=(10,0),
            textcoords='offset points', ha='center', va='bottom')

#                      CB Phase                      #
rectangularCurrent_CB = rectangularCurrent_C + rectangularCurrent_B
x = cmath.polar(rectangularCurrent_CB)
plt.polar([0,(x[1])],[0,mapRange(x[0],0,20,0,125)],marker='*',color='gold',linestyle = '-')
plt.polar([0,(x[1])],[0,mapRange(x[0],0,20,0,125)],marker=' ',color='navy',linestyle = '--')
ax.annotate(r'$I_{BC}$', xy=(x[1], mapRange(x[0],0,20,0,125)), xytext=(10,0),
            textcoords='offset points', ha='center', va='bottom')

#                      Power AB Phase                      #
rectangularPower_AB_A = rectangularCurrent_AB * rectangularVolts_A

x = cmath.polar(rectangularPower_AB_A)
plt.polar([0,(x[1])],[0,mapRange(x[0],0,1100,0,125)],marker='x',color='grey',linestyle = '-')
ax.annotate(r'$P_{AB}$', xy=(x[1], mapRange(x[0],0,1100,0,125)), xytext=(10,0),
            textcoords='offset points', ha='center', va='bottom')


#                      Power CB Phase                      #
rectangularPower_CB_C = rectangularCurrent_CB * rectangularVolts_C
x = cmath.polar(rectangularPower_CB_C)
plt.polar([0,(x[1])],[0,mapRange(x[0],0,1100,0,125)],marker='x',color='grey',linestyle = '-')
ax.annotate(r'$P_{CB}$', xy=(x[1], mapRange(x[0],0,1100,0,125)), xytext=(10,0),
            textcoords='offset points', ha='center', va='bottom')


plt.show()

