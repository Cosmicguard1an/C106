import plotly.express as px
import csv

with open('coffee.csv') as csvFile:
    df = csv.DictReader(csvFile)
    fig = px.scatter(df, x='Coffee in ml',y='sleep in hours',color='week')
    fig.show()
