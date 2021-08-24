import pandas as pd
import csv

import plotly.graph_objects as go 


df = pd.read_csv('C:/Users/aadi_/Desktop/coding/python/dataVisulation/data1.csv')
sid = df['student_id'].tolist()

newSdf = []

for i in range(168):
  sdf = df.loc[df['student_id'] == i]
  newSdf.append(sdf)



fig = go.Figure(go.Scatter(

    x = newSdf,
    y = ['Level 1','Level 2','Level 3','Level 4'],
    orientation = 'h'
))

fig.show()