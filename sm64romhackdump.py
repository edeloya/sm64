import requests
import pprint
import os
import re
import pandas as pd
from bs4 import BeautifulSoup

# Change current dir to script dir
pydir = os.path.dirname(os.path.abspath(__name__))
os.chdir(pydir)

# Panda term width
pd.set_option('display.max_colwidth', None)

# Read csv
df = pd.read_csv('sm64romhacks.lst', delimiter=',')
html_modname_list = [list(row) for row in df.values]
links = []

for gaem in html_modname_list:
    data = requests.get(gaem[0]).text
    soup = BeautifulSoup(data, 'lxml')
    table = soup.find('table')
    df = pd.read_html(str(table))[0].rename({'Starcount': 'Stars', 'Date (Format: yyyy-mm-dd)': 'Date'}, axis=1)
    for row in table.findAll("tr"):
        for cell in row.findAll("a"):
            link = re.sub(r"../../", "https://sm64romhacks.com/", cell['href'])
            links.append(repr(link))
    df1 = df[df.columns[:2]]
    df1.insert(2, 'Download', links)
    df2 = df[df.columns[3:]]
    df0 = df1.join(df2)
    with open('{}\\{}'.format(pydir,'output.txt'), 'a', encoding='utf-8') as logfile:
            logfile.write('{}\n\n{}\n\n'.format(df0.to_string(), 90*'-'))
    links.clear()


# ---testing---
# data = requests.get("https://sm64romhacks.com/hacks/24_hour_hack").text
# soup = BeautifulSoup(data, 'lxml')
# table = soup.find('table')
# df = pd.read_html(str(table))[0].rename({'Starcount': 'Stars', 'Date (Format: yyyy-mm-dd)': 'Date'}, axis=1)
# for row in table.findAll("tr"):
#     for cell in row.findAll("a"):
#         links.append(re.sub(r"../../", "https://sm64romhacks.com/", cell['href']))

# df1 = df[df.columns[:2]]
# df1.insert(2, 'Download', links)
# df2 = df[df.columns[3:]]
# df0 = df1.join(df2)


# table column examples
# df.info()
# df[['Hackname','Version','Creator', 'Starcount', 'Date (Format: yyyy-mm-dd)']]
# df1 = df[df.columns[:2]]
# df1.join(df2)
# df2.rename({'Starcount': '⭐', 'Date (Format: yyyy-mm-dd)': 'Date'}, axis=1)
