'''
    Catherine Romanova
    Kieran Croucher
    DS 2000
    Sp 2019
'''

import matplotlib.pyplot as plt
import numpy as np
import csv

def create_scatter_plot(years, storm_list, fatalities_list):
    plt.scatter(storm_list, fatalities_list, color='b')
    plt.xlabel('Number of Tornadoes')
    plt.ylabel('Number of Fatalities')
    plt.title('Number of Tornadoes vs Fatalities')
    plt.show()
