import pandas as pd
import matplotlib.pyplot as plt

livestock_price_regionXI = pd.read_csv(
    '2M4AFN10.csv',
    skiprows=2,
    sep=';',
    na_values=['..', '*/', '2/']
)

# print(livestock_price_regionXI.head())

livestock_price_regionXI.rename(columns={
    'Geolocation': 'province',
    'Type': 'commodity'
}, inplace=True)

df_long = livestock_price_regionXI.melt(
    id_vars=['province', 'commodity'],
    var_name='month_year',
    value_name='price'
)

df_long['date'] = pd.to_datetime(df_long['month_year'], format='%Y %B')
df_long['province'] = df_long['province'].str.strip('.')  .str.strip()

df_long = df_long.drop(columns='month_year').sort_values(['province', 'commodity', 'date']).reset_index(drop=True)



print(df_long.head(20))
# print(df_long['price'].dtypes)
# print(df_long.duplicated().sum())
# print(df_long['province'].unique())

summary_df = df_long.groupby(['province', 'commodity']).agg(
    mean_price=('price', 'mean')
)
# print(summary_df[summary_df['mean_price'] == summary_df['mean_price'].max()])


#Line chart of the most highest mean price commodity in Davao Region 
subset_df = df_long[
    (df_long['province'] == 'Davao Occidental') &
    (df_long['commodity'] == 'Duck egg')
].dropna(subset=['price'])

subset_df.plot(x='date', y='price', kind='line', title='Duck Egg Prices in Davao Occidental')
plt.show()

#Line chart for the commodities in Davao de Oro
Davao_de_Oro_df = df_long[
    (df_long['province'] == 'Davao de Oro')
].dropna(subset=['price'])

pivot_DDO_df = Davao_de_Oro_df.pivot(index='date', columns='commodity', values='price')
pivot_DDO_df.plot(title='Commodity Prices in Davao de Oro')
plt.show()