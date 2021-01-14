#!/usr/bin/env python3
#
# Christopher Rodriguez
# CPSC 223p-03
# 2020-10-22
# chrisrod46@csu.fullerton.edu
#
"""This program will take in a JSON file and output a plot using the date
in the JSON file"""
import json
import sys
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates
import matplotlib.cbook as cbook
from datetime import datetime
from time import sleep

def main():
    """This function will take in an input file and plot the misery index"""

    dates = []
    umploy = []
    inflate = []
    misery = []

    file = sys.argv[1]
    with open(file, 'r') as fp:
        data = json.load(fp)

    for i in range(len(data['dataset_data']['data'])):
        dates.append(datetime.strptime(data['dataset_data']['data'][i][0],\
        "%Y-%m-%d").date().year)
        umploy.append(data['dataset_data']['data'][i][1])
        inflate.append(data['dataset_data']['data'][i][2])
        misery.append(data['dataset_data']['data'][i][3])

    fig, ax = plt.subplots()
    ax.plot(dates, umploy, label = "Unemployment Rate")
    ax.plot(dates, inflate, label = "Inflation Rate", color = "purple")
    ax.plot(dates, misery, label = "Misery Index", color = "red")
    ax.set(xlabel='Date (yyyy)', ylabel='Rate', \
    title='Misery Index numbers')

    ax.grid()
    ax.legend()

    fig.autofmt_xdate()
    ax.fmt_xdata = mdates.DateFormatter('%Y-%m-%d')
    fig.savefig("us_misery_plot.pdf")
    print("Done")


if __name__ == "__main__":
    main()
