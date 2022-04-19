import requests, pprint, os, re
import pandas as pd
from bs4 import BeautifulSoup
pydir = os.path.dirname(os.path.abspath(__name__))         #Change current dir to script dir
df = pd.read_csv('sm64romhacks.lst', delimiter=',')        #Read csv
html_modname_list = [list(row) for row in df.values]
links = []

# for gaem in html_modname_list:
#     data = requests.get(gaem[0]).text
#     # data = requests.get("https://sm64romhacks.com/hacks/sm64_lost_worlds_remake").text    #Testing
#     soup = BeautifulSoup(data, 'lxml')
#     table = soup.find('table')
#     df = pd.read_html(str(table))[0]
#     for tr in table.findAll("tr"):
#         trs = tr.findAll("td")
#         for each in trs:
#             try:
#                 link = each.find('a')['href']
#                 links.append(re.sub(r"../../", "https://sm64romhacks.com/", link))
#             except:
#                 pass
#     with open('{}\\{}'.format(pydir,'output.txt'), 'a', encoding='utf-8') as logfile:
#             logfile.write('{}\n\n{}\n\n\n{}\n\n\n'.format(pprint.pformat(df), pprint.pformat(links), 90*'-'))
#     links.clear()



# ---single page copypasta test---

data = requests.get("https://sm64romhacks.com/hacks/sm64_lost_worlds_remake").text
soup = BeautifulSoup(data, 'lxml')
table = soup.find('table')
df = pd.read_html(str(table))[0]
for tr in table.findAll("tr"):
    trs = tr.findAll("td")
    for each in trs:
        try:
            link = each.find('a')['href']
            links.append(re.sub(r"../../", "https://sm64romhacks.com/", link))
        except:
            pass

# #with open('{}\\{}'.format(pydir,'output.txt'), 'a', encoding='utf-8') as logfile:
# #        logfile.write('{}\n\n{}\n\n\n{}\n\n\n'.format(pprint.pformat(df), pprint.pformat(links), 90*'-'))