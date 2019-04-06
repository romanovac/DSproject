'''
    Catherine Romanova
    Kieran Croucher
    DS 2000
    Sp 2019
'''

import matplotlib.pyplot as plt
import numpy as np
from vis_scatter import create_scatter_plot
from vis_scatter2 import create_scatter2_plot

import csv

def format_data(details_dict):
    storm_num_list = []
    for year in details_dict.keys():
        data = details_dict[year]
        storm_num_list.append(data)

    return storm_num_list

def format_fatalities(fatalities_dict):
    fatalities_list = []
    for year in fatalities_dict.keys():
        data = fatalities_dict[year]
        fatalities_list.append(data[0])

    return fatalities_list

def format_injuries(fatalities_dict):
    injuries_list = []
    for year in fatalities_dict.keys():
        data = fatalities_dict[year]
        injuries_list.append(data[1])

    return injuries_list


def create_bar_chart(years, storm_list, fatalities_list):
    N = len(years)
    ind = np.arange(N)
    width = 0.3
    plt.bar(ind - width, storm_list, width, color='b', align='center')
    plt.bar(ind, fatalities_list, width, color='r', align='center')
    plt.xlabel('Year')
    plt.ylabel('Amount')
    plt.xticks(ind, years)
    plt.title('Number of Tornadoes, Fatalities, and Injuries Per Year')
    labels = ['Tornadoes', 'Fatalities', 'Injuries']
    plt.legend(labels)
    plt.show()


def vis_driver(num_storms_dict, num_fatalities_dict):
    storm_list = format_data(num_storms_dict)
    injuries_list = format_injuries(num_fatalities_dict)
    fatalities_list = format_fatalities(num_fatalities_dict)
    create_bar_chart(list(num_storms_dict.keys()), storm_list,
                    fatalities_list)
    create_scatter_plot(list(num_storms_dict.keys()), storm_list,
                        fatalities_list)

