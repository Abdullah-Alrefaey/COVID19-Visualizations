import plotly
import plotly.graph_objs as go
# import plotly.plotly as py
import csv

with open("Data.csv") as csvFile:
    csv_reader = csv.DictReader(csvFile)
    line_count = 0
    dataTuple = []
    dataList = [[], [], []]
    for row in csv_reader:
        dataTuple.append((row['Country'], row['Age'], row['Salary']))
    print(dataTuple)
    for tup in dataTuple:
        dataList[0].append(tup[0])
        dataList[1].append(tup[1])
        dataList[2].append(tup[2])
    print(dataList)

# dataList[0].sort()


trace1 = go.Bar(
                x = df_groupby_datebr.index.values,
                y = df_groupby_datebr.ZHVI_1bedroom,
                name = "ZHVI_1bedroom",
                marker = dict(color = 'rgb(102,255,255)'),
                text = df_groupby_datebr['ZHVI_1bedroom'])

data = [trace1]
layout = go.Layout(barmode = "group", title="Bar Chart: Mean House Values by Bedrooms and Year",
                   xaxis= dict(title= 'Year',ticklen= 5,zeroline= False),
                   yaxis= dict(title= 'Mean House Values',ticklen= 5,zeroline= False))
fig = go.Figure(data = data, layout = layout)
url = py.plot(fig, validate=False)
