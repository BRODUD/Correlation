import pandas as pd
import plotly.express as px
import numpy as np
import csv

path = 'D:\Documents\school\jr\PRIVATE\Python\Project 106\File1.csv'
# Showing Scatter Graph
with open(path, newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)

#To remove headers from CSV
file_data.pop(0)


total_marks = 0
total_entries = len(file_data)

for marks in file_data:
    total_marks+= float(marks[1])

mean = total_marks/total_entries


def plotFigure(data_path,x_data,y_data):
    df = pd.read_csv(data_path)
    fig = px.scatter(df,x=x_data,y=y_data)
    fig.update_layout(shapes=[
    dict(
        type = 'line',
        y0=mean ,
        y1 = mean,
        x0=0,
        x1=30
    )
    ])
    fig.show()

def getDataSource(data_path,x_data,y_data):
    marks = []
    days=[]
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            marks.append(float(row[y_data]))
            days.append(float(row[x_data]))

    return {"x" : days, "y": marks}


def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource["x"],dataSource["y"])
    print("Correlation between Attendance and Marks :-  \n--->",correlation[0,1])


def main():
    data_path = path
    x_data= 'Days'
    y_data= 'Marks'

    datasource = getDataSource(data_path,x_data,y_data)
    findCorrelation(datasource)
    plotFigure(data_path,x_data,y_data)


main()
    