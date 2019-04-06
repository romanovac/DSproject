'''
    Catherine Romanova
    Kieran Croucher
    DS 2000
    Sp 2019
'''
'''
make a dictionary to count number of storms for each year and number of
injuries/deaths
'''

import csv
from vis import vis_driver

def count_storms(details_dict):
    num_storms_dict = {}
    for year in details_dict.keys():
        year_details = details_dict[year]
        count = 0
        for row in year_details:
            count = count + 1
        num_storms_dict[year] = count

    return num_storms_dict

def count_fatalities(fatalities_dict, details_dict):
    ''' the first value in the dict is deaths, second value is injuries
    '''
    num_fatalities_dict = {}
    for year in details_dict.keys():
        year_data = []
        year_details = details_dict[year]
        fatalities_details = fatalities_dict[year]
        count_injuries = 0
        count_deaths = 0
        for row in year_details:
            storm_id = row[7]
            for row in fatalities_details:
                if(row[4] == storm_id):
                    if(row[5] == 'D'):
                        count_deaths = count_deaths + 1
                    else:
                        count_injuries = count_injuries + 1
        year_data.append(count_deaths)
        year_data.append(count_injuries)
        num_fatalities_dict[year] = year_data

    return num_fatalities_dict
        

def find_average(details_dict):
    total_storms_num = 0
    count = 0
    for year in details_dict.keys():
        total_storms_num = total_storms_num + details_dict[year]
        count = count + 1

    return round(total_storms_num / count, 2)

def find_avg_fatalities(fatalities_dict):
    total_deaths_num = 0
    total_injuries_num = 0
    count = 0
    for year in fatalities_dict.keys():
        total_deaths_num = total_deaths_num + fatalities_dict[year][0]
        total_injuries_num = total_injuries_num + fatalities_dict[year][1]
        count = count + 1

    return round(total_deaths_num / count, 2), round(total_injuries_num / count, 2)

def open_fatalities():
    ''' Opens all the fatalities csv files and loads them into a dictionary,
        where the key is the year and the file info is the value"
    '''
    filename_fatalities = 'storm_fatalities_'
    filename_year = 1997
    i = 0
    fatalities_dict = {}
    
    while i < 21:
        filename_year = filename_year + 1
        filename = filename_fatalities + str(filename_year) + ".csv"
        
        with open(filename, "r") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            fatalities_data = []
            for row in csv_reader:
                fatalities_data.append(row)
                
        fatalities_dict[filename_year] = fatalities_data
        i = i + 1

    return fatalities_dict


def open_details():
    ''' Opens all the details csv files and loads them into a dictionary,
        where the key is the year and the file info is the value"
    '''
    filename_details = 'storm_details_'
    filename_year = 1997
    i = 0
    details_dict = {}
    
    while i < 21:
        filename_year = filename_year + 1
        filename = filename_details + str(filename_year) + ".csv"
        
        with open(filename, "r") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            details_data = []
            for row in csv_reader:
                if(row[12] == 'Tornado'):
                    details_data.append(row)
        details_dict[filename_year] = details_data
        i = i + 1

    return details_dict

def process_files():
    fatalities_dict = open_fatalities()
    details_dict = open_details()
    num_storms_dict = count_storms(details_dict)
    num_fatalities_dict = count_fatalities(fatalities_dict, details_dict)
    avg_storm_num = find_average(num_storms_dict)
    avg_deaths, avg_injuries = find_avg_fatalities(num_fatalities_dict)

    vis_driver(num_storms_dict, num_fatalities_dict)
    
def main():
    process_files()

main()
