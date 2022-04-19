# Objective
Crawl https://sm64romhacks.com for zips and catalogue versions and their metadata

# Pre-requisites:
Python3

```
pip install pandas
pip install lxml
```

# To Investigate:
- How do we determine the most recent / supported version of a romhack when dates are missing?
  - Some version names are a bit more complex than simply incrementing a number(s)
- Can we automate unzipping, folder structure, patching, and checksumming with our own backup ROM?
- How do we decide filenames for romhacks which were named with illegal characters?
  - `\ / ? : " < > |`
- Which characters does EverDrive, Project64, etc support?

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