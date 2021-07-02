import plotly.express as px
import csv
import numpy as np

with open("cups of coffee vs hours of sleep.csv") as csv_file:
    df = csv.DictReader(csv_file)
    fig = px.scatter(df, x = "Coffee in ml",y = "sleep in hours")
    fig.show()

def getDataSource(data_path):
    coffee = []
    sleep = []
    with open(data_path) as f:
        csv_reader = csv.DictReader(f)
        for row in csv_reader:
            coffee.append(float(row["Coffee in ml"]))
            sleep.append(float(row["sleep in hours"]))
    return {"x":coffee, "y":sleep}

def find_correlation(data_source):
    correlation = np.corrcoef(data_source["x"],data_source["y"])
    print("Correlation between Cups of Coffee and hours of sleep = ",correlation[0,1])

def setup():
    data_path = "cups of coffee vs hours of sleep.csv"

    data_source = getDataSource(data_path)
    find_correlation(data_source)

setup()