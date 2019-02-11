import math
import cmath

import numpy as np
import matplotlib.pyplot as plt

def mapRange (x, from_min, from_max, to_min, to_max):
    return (x - from_min) * (to_max - to_min) / (from_max - from_min) + to_min

class ThreePhase_FourWire:
    def __init__(self):
        self.x = ''


    def create_graph(rectangularVolts_A,rectangularCurrent_A,
                     rectangularVolts_B,rectangularCurrent_B,
                     rectangularVolts_C,rectangularCurrent_C,curent_scale,voltage_sclae):
        #creates the plot for the polar graph
        fig = plt.figure()
        ax = fig.add_subplot(111, polar=True)
        ax.set_rmax(5.05)
        z = np.array([r'$E_{NC}$', r'$E_{AC}$', r'$E_{AN}$',
                      r'$E_{AB}$', r'$E_{NB}$', r'$E_{CB}$',
                      r'$E_{CN}$', r'$E_{CA}$', r'$E_{NA}$',
                      r'$E_{BA}$', r'$E_{BN}$', r'$E_{BC}$'])
        plt.xticks([0, 0.523598776, 1.047197551, 1.570796327, 2.094395102,
                    2.617993878, 3.141592654, 3.665191429, 4.188790205,
                    4.71238898, 5.235987756, 5.759586532], z)
        ax.set_rgrids([], angle=345.)
        fig.set_size_inches(8, 8, forward=False)



        #                        Graph                      #
        #                      A Phase                      #
        x = cmath.polar(rectangularVolts_A)
        plt.polar([0,(x[1])],[0,x[0]],marker='p',color='red')
        ax.annotate(r'$E_{AN}$', xy=(x[1], x[0]), xytext=(10,0),
                    textcoords='offset points', ha='center', va='bottom')
        x = cmath.polar(rectangularCurrent_A)
        plt.polar([0,(x[1])],[0,mapRange(x[0],0,20,0,125)],marker='*',color='firebrick')
        ax.annotate(r'$I_{A}$', xy=(x[1], mapRange(x[0],0,20,0,125)), xytext=(10,0),
                    textcoords='offset points', ha='center', va='bottom')

        #                      B Phase                      #
        x = cmath.polar(rectangularVolts_B)
        plt.polar([0,(x[1])],[0,x[0]],marker='p',color='yellow')
        ax.annotate(r'$E_{AN}$', xy=(x[1], x[0]), xytext=(10,0),
                    textcoords='offset points', ha='center', va='bottom')
        x = cmath.polar(rectangularCurrent_B)
        plt.polar([0,(x[1])],[0,mapRange(x[0],0,20,0,125)],marker='*',color='gold')
        ax.annotate(r'$I_{B}$', xy=(x[1], mapRange(x[0],0,20,0,125)), xytext=(10,0),
                    textcoords='offset points', ha='center', va='bottom')

        #                      C Phase                      #
        x = cmath.polar(rectangularVolts_C)
        plt.polar([0,(x[1])],[0,x[0]],marker='p',color='blue')
        ax.annotate(r'$E_{CN}$', xy=(x[1], x[0]), xytext=(10,0),
                    textcoords='offset points', ha='center', va='bottom')

        x = cmath.polar(rectangularCurrent_C)
        plt.polar([0,(x[1])],[0,mapRange(x[0],0,20,0,125)],marker='*',color='navy')
        ax.annotate(r'$I_{C}$', xy=(x[1], mapRange(x[0],0,20,0,125)), xytext=(10,0),
                    textcoords='offset points', ha='center', va='bottom')

        dictForLegend = []
        dictForLegend = [plt.polar([0,0],[0,0],marker='p',color='black', label='Current Element'),
                         plt.polar([0,0],[0,0],marker='*',color='black', label='Voltage Element'),
                         plt.polar([0,0],[0,0], marker=' ', color='black', linestyle='--', label='Sum of Currents')]


        plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),shadow=True, ncol=2)


        plt.show()

