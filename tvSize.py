import numpy as np
import csv

def getDataSource(datapath):
    tvSize = []
    avgTime= []
    with open(datapath) as csvFile:
        df = csv.DictReader(csvFile)
        for row in df:
            tvSize.append(float(row["Size of TV"]))
            avgTime.append(float(row["Average time spent watching TV in a week (hours)"]))
    
    return {'x': tvSize, 'y': avgTime}

def correlation(dataSource):
    corr = np.corrcoef(dataSource['x'],dataSource['y'])
    print('Correlation between tv size and average time',corr[0,1])

def setup():
    datapath = "TV.csv"
    dataSource = getDataSource(datapath)
    correlation(dataSource)

setup()