import numpy as np
import csv

def getDataSource(datapath):
    iceCreamSales = []
    coldDrinkSales = []
    with open(datapath) as csvFile:
        df = csv.DictReader(csvFile)
        for row in df:
            iceCreamSales.append(float(row["Temperature"]))
            coldDrinkSales.append(float(row["Ice-cream Sales"]))
    
    return {'x': iceCreamSales, 'y': coldDrinkSales}

def correlation(dataSource):
    corr = np.corrcoef(dataSource['x'],dataSource['y'])
    print('Correlation between temperature and ice cream',corr[0,1])

def setup():
    datapath = "iceCream.csv"
    dataSource = getDataSource(datapath)
    correlation(dataSource)

setup()