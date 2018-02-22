import matplotlib.pyplot as plt
import numpy as np

# part one
'''import csv

x=[]
y=[]

with open('example','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(int(row[0]))
        y.append(int(row[1]))

plt.plot(x,y)
'''

# x,y = np.loadtxt('example', delimiter=',', unpack=True)
# plt.plot(x,y, label='Loaded from file')

# from internet
import urllib
import matplotlib.dates as mdates


def bytespdate2num(fmt, encoding='utf-8'):
    strconverter = mdates.strpdate2num(fmt)

    def bytesconverter(b):
        s = b.decode(encoding)
        return strconverter(s)

    return bytesconverter


def graph_data(stock):

    fig = plt.figure()
    ax1 = plt.subplot2grid((1,1),(0,0))
    stock_price_url = 'https://pythonprogramming.net/yahoo_finance_replacement'

    source_code = urllib.urlopen(stock_price_url).read().decode()

    stock_data = []
    split_source = source_code.split('\n')

    for line in split_source[1:]:
        split_line = line.split(',')
        if len(split_line) == 7:
            if 'values' not in line:
                stock_data.append(line)

    date, openp, highp, lowp, closep, adj_closep, volume = np.loadtxt(stock_data,
                                                                      delimiter=',',
                                                                      unpack=True,
                                                                      converters={0: bytespdate2num('%Y-%m-%d')})

    ax1.plot_date(date, closep, '-', label='Price')

    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(45)

    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('Interesting graph\nfrom net')
    plt.legend()
    plt.show()


graph_data('TSLA')