import plotly.express as px
import csv

with open('iceCream.csv') as csvFile:
    df = csv.DictReader(csvFile)
    fig = px.scatter(df, x='Temperature',y='Ice-cream Sales')
    fig.show()
