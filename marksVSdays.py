import pandas as pd
import plotly.express as pe
import numpy as np

data = pd.read_csv("marksVSdays.csv")

marks = data["Marks In Percentage"].tolist()

presentDays = data["Days Present"].tolist()

graph = pe.scatter(data, x = presentDays , y = marks)

correlation = np.corrcoef(presentDays, marks)

print("correlation : " ,  correlation[0 , 1])












