import pandas as pd

livestock_price_regionXI = pd.read_csv(
    '2M4AFN10.csv', 
    skiprows=2,
    sep=';',
    na_values='..'
    )

print(livestock_price_regionXI.head())





