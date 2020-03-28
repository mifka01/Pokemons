import requests
from bs4 import BeautifulSoup
import json


experiences = {}
result = requests.get('https://bulbapedia.bulbagarden.net/wiki/Experience')
source = result.content
soup = BeautifulSoup(source, 'lxml')
table = soup.find("table", {"class": "roundy"})
trs = table.find_all("tr")

heading = list(set([th.text.replace("\n","").replace(" ","").replace("-","") for th in trs[1].find_all("th")]))
heading.remove("Level")

levels = range(1, 101)
print(heading)
erratic = {}
fast = {}
medium_fast = {}
medium_slow = {}
slow = {}
fluctuating = {}

for lv in levels:
    fast_num = (4 * (lv**3)) / 5
    fast[int(fast_num)] = lv
    if lv <= 50:
        erratic_num = (lv**3 * (100-lv)) / 50
        erratic[int(erratic_num)] = lv
    if lv > 50 and lv<= 68:
        erratic_num = (lv**3 * (150-lv)) / 100
        erratic[int(erratic_num)] = lv
    if lv > 68 and lv<= 98:
        erratic_num = (lv**3* ((1911-10*lv)/3) ) / 500
        erratic[int(erratic_num)] = lv
    if lv > 98 and lv<= 100:
        erratic_num = (lv**3* (160-lv)) / 100
        erratic[int(erratic_num)] = lv

    medium_fast_num = lv**3
    medium_fast[int(medium_fast_num)] = lv

    medium_slow_num = ((6/5)*lv**3) - 15*lv**2 + 100*lv -140
    medium_slow[int(medium_slow_num)] = lv

    slow_num = (5*lv**3) / 4
    slow[int(slow_num)] = lv

    if lv <=15:
        fluctuating_num = lv**3 * ((((lv+1)/3) +24)/50)  
        fluctuating[int(fluctuating_num)] = lv
    if lv >15 and lv <= 36:
        fluctuating_num = lv**3 * ((lv + 14)/50)
        fluctuating[int(fluctuating_num)] = lv
    if lv >36 and lv <= 100:
        fluctuating_num = lv**3 * (((lv/2)+32)/50)
        fluctuating[int(fluctuating_num)] = lv
      
data_grow = [medium_slow, medium_fast, slow, erratic, fluctuating,fast]
for head, data in zip(heading,data_grow):
    experiences[head] = data
with open("data/experiences.json", 'w') as f:
    json_object = json.dumps(experiences, sort_keys=True, indent=4)
    f.write(json_object)