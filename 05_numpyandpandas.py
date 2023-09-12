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