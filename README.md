# Objective
Crawl https://sm64romhacks.com for zips and catalogue versions and their metadata

# Pre-requisites:
Python3

```
pip install pandas
pip install lxml
```
# Notes:
[Pandas documentation on DataFrames](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html?highlight=dataframe#pandas.DataFrame)

## DataFrame Examples:

```
df.info()
df.count()
df[['Hackname','Version','Creator', 'Starcount', 'Date (Format: yyyy-mm-dd)']]# df1 = df[df.columns[:2]]
df1.join(df2)
df2.rename({'Starcount': '⭐', 'Date (Format: yyyy-mm-dd)': 'Date'}, axis=1)
```