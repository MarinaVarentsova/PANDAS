import pandas as pd
data = pd.read_csv('california_housing_train.csv')
# print(data.dtypes)
# Задача 42: Узнать какая максимальная households в зоне минимального значения population.
print(data[data['population'] == data['population'].min()]['households'].max())
