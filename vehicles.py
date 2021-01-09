import pandas as pd

vehicles = pd.read_csv('/data/vehicles.csv', sep=',')

print(vehicles.shape)
