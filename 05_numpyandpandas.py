import pandas as pd
import numpy as np

# a = np.arange(5)

# print(a)

# a = np.arange(4)
# print(a)

# b = np.array([10, 10, 10 ,10])

# c = a * b - 8


# dataframes
df = pd.DataFrame({
    "Population" : [35.467, 63.951, 80.94, 60.665, 127.061, 64.511, 318.523],
    "GDP" : [
        1785387,
        2833687,
        3874437, 
        2167744,
        4602367,
        2950039,
        17348075
    ],
    "Surface" : [
        9984670,
        640679,
        357114,
        301336,
        377930,
        242495,
        9525067  
    ],
    "HDI" : [0.913 , 0.888, 0.916, 0.873, 0.891, 0.907, 0.915],
    "Continent" : ['America', 'Europe', 'Europe', 'Europe', 'Asia', 'Europe', 'America']
})

print(df)

g7_pop = pd.Series([35.453 , 63.1523, 78.643, 96.1385])
# print(g7_pop)

g7_pop.name = 'G7 pupulation in million'
# print(type(g7_pop.values))

certificates_earned = pd.Series(
    [8, 2, 5, 6],
    index=['Tom', 'Kris', 'Ahmad', 'Beau']
)

# print(certificates_earned)

g7_pop.index = ['Canada', 'France', 'United State', 'Brasil']

print(g7_pop)