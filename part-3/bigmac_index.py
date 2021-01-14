#!/usr/bin/env python3
#
# Christopher Rodriguez
# CPSC 223p-03
# 2020-10-22
# chrisrod46@csu.fullerton.edu
#

"""This program will take in a CSV file and plot the CSV file into
three different pdfs"""
import sys
import csv
import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.axisartist.axislines import SubplotZero
import numpy as np
import matplotlib.dates as mdates
import matplotlib.cbook as cbook
from datetime import datetime
from time import sleep
import math

def main():
    """The main function will take in all countries csv files and use the
    date to graph different kinds of plots"""

    fields = []
    rows = []
    CAN_years = []
    CHN_years = []
    DEU_years = []
    JPN_years = []
    MEX_years = []
    NZL_years = []
    USA_years = []
    CAN_dollar_adj = []
    CAN_dollar_val = []
    CHN_dollar_adj = []
    CHN_dollar_val = []
    DEU_dollar_adj = []
    DEU_dollar_val = []
    JPN_dollar_adj = []
    JPN_dollar_val = []
    MEX_dollar_adj = []
    MEX_dollar_val = []
    NZL_dollar_adj = []
    NZL_dollar_val = []
    us = []
    country = []
    min_wage = []
    hours_req = []
    CAN_2017 = 0.0
    CHN_2017 = 0.0
    DEU_2017 = 0.0
    JPN_2017 = 0.0
    MEX_2017 = 0.0
    NZL_2017 = 0.0
    USA_2017 = 0.0


    # reading csv file
    with open("ECONOMIST-BIGMAC_CAN.csv", 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        fields = next(csvreader)
        for row in csvreader:
            rows.append(row)
    #create a plot that goes from 2000 to 2020
    for i in range(len(rows)):
        CAN_years.append(datetime.strptime(rows[i][0],\
        "%Y-%m-%d").date().year)
        CAN_dollar_val.append(rows[i][5])
        us.append(0)
        if rows[i][6] != '':
            CAN_dollar_adj.append(float(rows[i][6]))
        if CAN_dollar_val[i] != '':
            CAN_dollar_val[i] = float(CAN_dollar_val[i])
        if CAN_years[i] == 2017 and CAN_2017 == 0.0:
            CAN_2017 = float(rows[i][3])
    rows.clear()
    fields.clear()

    # reading csv file
    with open("ECONOMIST-BIGMAC_CHN.csv", 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        fields = next(csvreader)
        for row in csvreader:
            rows.append(row)
    for i in range(len(rows)):
        CHN_years.append(datetime.strptime(rows[i][0],\
        "%Y-%m-%d").date().year)
        CHN_dollar_val.append(rows[i][5])
        if rows[i][6] != '':
            CHN_dollar_adj.append(float(rows[i][6]))
        if CHN_dollar_val[i] != '':
            CHN_dollar_val[i] = float(CHN_dollar_val[i])
        if CHN_years[i] == 2017 and CHN_2017 == 0.0:
            CHN_2017 = float(rows[i][3])
    rows.clear()
    fields.clear()
    # reading csv file
    with open("ECONOMIST-BIGMAC_DEU.csv", 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        fields = next(csvreader)
        for row in csvreader:
            rows.append(row)
    #create a plot that goes from 2000 to 2020
    for i in range(len(rows)):
        DEU_years.append(datetime.strptime(rows[i][0],\
        "%Y-%m-%d").date().year)
        DEU_dollar_val.append(rows[i][5])
        if rows[i][6] != '':
            DEU_dollar_adj.append(float(rows[i][6]))
        if DEU_dollar_val[i] != '':
            DEU_dollar_val[i] = float(DEU_dollar_val[i])
        if DEU_years[i] == 2017 and DEU_2017 == 0.0:
            DEU_2017 = float(rows[i][3])
    rows.clear()
    fields.clear()
    # reading csv file
    with open("ECONOMIST-BIGMAC_JPN.csv", 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        fields = next(csvreader)
        for row in csvreader:
            rows.append(row)
    #create a plot that goes from 2000 to 2020
    for i in range(len(rows)):
        JPN_years.append(datetime.strptime(rows[i][0],\
        "%Y-%m-%d").date().year)
        JPN_dollar_val.append(rows[i][5])
        if rows[i][6] != '':
            JPN_dollar_adj.append(float(rows[i][6]))
        if JPN_dollar_val[i] != '':
            JPN_dollar_val[i] = float(JPN_dollar_val[i])
        if JPN_years[i] == 2017 and JPN_2017 == 0.0:
            JPN_2017 = float(rows[i][3])
    rows.clear()
    fields.clear()
    # reading csv file
    with open("ECONOMIST-BIGMAC_MEX.csv", 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        fields = next(csvreader)
        for row in csvreader:
            rows.append(row)
    #create a plot that goes from 2000 to 2020
    for i in range(len(rows)):
        MEX_years.append(datetime.strptime(rows[i][0],\
        "%Y-%m-%d").date().year)
        MEX_dollar_val.append(rows[i][5])
        if rows[i][6] != '':
            MEX_dollar_adj.append(float(rows[i][6]))
        if MEX_dollar_val[i] != '':
            MEX_dollar_val[i] = float(MEX_dollar_val[i])
        if MEX_years[i] == 2017 and MEX_2017 == 0.0:
            MEX_2017 = float(rows[i][3])
    rows.clear()
    fields.clear()

    # reading csv file
    with open("ECONOMIST-BIGMAC_MEX.csv", 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        fields = next(csvreader)
        for row in csvreader:
            rows.append(row)
    #create a plot that goes from 2000 to 2020
    for i in range(len(rows)):
        NZL_years.append(datetime.strptime(rows[i][0],\
        "%Y-%m-%d").date().year)
        NZL_dollar_val.append(rows[i][5])
        if rows[i][6] != '':
            NZL_dollar_adj.append(float(rows[i][6]))
        if NZL_dollar_val[i] != '':
            NZL_dollar_val[i] = float(NZL_dollar_val[i])
        if NZL_years[i] == 2017 and NZL_2017 == 0.0:
            NZL_2017 = float(rows[i][3])
    rows.clear()
    fields.clear()

    # reading csv file
    with open("ECONOMIST-BIGMAC_USA.csv", 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        fields = next(csvreader)
        for row in csvreader:
            rows.append(row)
    #create a plot that goes from 2000 to 2020
    for i in range(len(rows)):
        USA_years.append(datetime.strptime(rows[i][0],\
        "%Y-%m-%d").date().year)
        if USA_years[i] == 2017 and USA_2017 == 0.0:
            USA_2017 = float(rows[i][3])
    rows.clear()
    fields.clear()


    fig, ax = plt.subplots(figsize=(10,10), sharex = True)

    ax.plot(CAN_years, CAN_dollar_val, dashes = [3, 2], label = "CAN_dollar_valuation", color = "red")
    ax.plot(CAN_years[0:len(CAN_dollar_adj)], CAN_dollar_adj, label = "CAN_dollar_adj_valuation", color = "red")

    ax.plot(CHN_years, CHN_dollar_val, dashes = [3, 2], label = "CHN_dollar_valuation", color = "blue")
    ax.plot(CHN_years[0:len(CHN_dollar_adj)], CHN_dollar_adj, label = "CHN_dollar_adj_valuation", color = "blue")

    ax.plot(DEU_years, DEU_dollar_val, dashes = [3, 2], label = "DEU_dollar_valuation", color = "yellow")
    ax.plot(DEU_years[0:len(DEU_dollar_adj)], DEU_dollar_adj, label = "DEU_dollar_adj_valuation", color = "yellow")

    ax.plot(JPN_years, JPN_dollar_val, dashes = [3, 2], label = "JPN_dollar_valuation", color = "green")
    ax.plot(JPN_years[0:len(JPN_dollar_adj)], JPN_dollar_adj, label = "JPN_dollar_adj_valuation", color = "green")

    ax.plot(MEX_years, MEX_dollar_val, dashes = [3, 2], label = "MEX_dollar_valuation", color = "purple")
    ax.plot(MEX_years[0:len(MEX_dollar_adj)], MEX_dollar_adj, label = "MEX_dollar_adj_valuation", color = "purple")

    ax.plot(NZL_years, NZL_dollar_val, dashes = [3, 2], label = "NZL_dollar_valuation", color = "orange")
    ax.plot(NZL_years[0:len(NZL_dollar_adj)], NZL_dollar_adj, label = "NLZ_dollar_adj_valuation", color = "orange")

    ax.plot(CAN_years, us, dashes = [6, 2], label = "U.S (0 percent)", color = "black")
    ax.set(xlabel='Date', ylabel='Percent Change', \
    title='Canada Index')
    plt.margins(0)
    ax.legend()
    fig.savefig("big_mac_index_valuation.pdf")
    plt.close(fig)


    #Making scatter plot
    fig, ax1 = plt.subplots()
    ax1.scatter(CAN_dollar_adj, CAN_years[0:len(CAN_dollar_adj)],\
    alpha = 0.5, label = "CAN_dollar_adj" , color = "red")
    ax1.scatter(CHN_dollar_adj, CHN_years[0:len(CHN_dollar_adj)],\
    alpha = 0.5, label = "CHN_dollar_adj" , color = "blue")
    ax1.scatter(DEU_dollar_adj, DEU_years[0:len(DEU_dollar_adj)],\
    alpha = 0.5, label = "DEU_dollar_adj" , color = "yellow")
    ax1.scatter(JPN_dollar_adj, JPN_years[0:len(JPN_dollar_adj)],\
    alpha = 0.5, label = "JPN_dollar_adj" , color = "green")
    ax1.scatter(MEX_dollar_adj, MEX_years[0:len(MEX_dollar_adj)],\
    alpha = 0.5, label = "MEX_dollar_adj" , color = "purple")
    ax1.scatter(NZL_dollar_adj, NZL_years[0:len(NZL_dollar_adj)],\
    alpha = 0.5, label = "NZL_dollar_adj" , color = "orange")
    ax1.plot(us, CAN_years, dashes = [6, 2], \
    label = "U.S (0 percent)", color = "black")
    ax1.set(xlabel='Percent Change', ylabel='Year', \
    title='Scatter Index')
    plt.margins(0)
    ax1.legend()
    fig.savefig("big_mac_index_scatter.pdf")
    plt.close(fig)

    with open("Minnimum_Wage.csv", 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        fields = next(csvreader)
        for row in csvreader:
            rows.append(row)

    for i in range(len(rows)):
        country.append(rows[i][0])
        min_wage.append(float(rows[i][1]))

    hours_req.append(math.ceil((CAN_2017 / min_wage[0]) * 4))
    hours_req.append(math.ceil((CHN_2017 / min_wage[1]) * 4))
    hours_req.append(math.ceil((DEU_2017 / min_wage[2]) * 4))
    hours_req.append(math.ceil((JPN_2017 / min_wage[3]) * 4))
    hours_req.append(math.ceil((MEX_2017 / min_wage[4]) * 4))
    hours_req.append(math.ceil((NZL_2017 / min_wage[5]) * 4))
    hours_req.append(math.ceil((USA_2017 / min_wage[6]) * 4))



    fig, ax2 = plt.subplots()
    ax2.bar(country, hours_req, color = "green")
    ax2.set(xlabel='country', ylabel='Hours needed', \
    title='Feed a familiy Index')
    fig.savefig("hours_worked_to_feed_a_family.pdf")


if __name__ == "__main__":
    main()
