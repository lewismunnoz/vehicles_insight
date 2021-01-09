import pandas as pd

vehicles = pd.read_csv('./data/vehicles.csv', sep=',')

print('How much big is this csv:', vehicles.size)
