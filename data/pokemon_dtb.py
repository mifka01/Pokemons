import requests
from bs4 import BeautifulSoup
import csv
import json

names = []
pokemons = {}
result = requests.get('https://pokemondb.net/pokedex/all')
source = result.content
soup = BeautifulSoup(source, 'lxml')
table = soup.find('table', id="pokedex")
trs = table.findChildren('tr')
ass = table.findAll("a", {"class": "ent-name"})

for a in ass:
    names.append(a.text.lower())
names = set(names)
names = ["bulbasaur","charmander"]


for name in names:
    base_stats = {}
    defense_stats = {}

    result = requests.get(f'https://pokemondb.net/pokedex/{name}')
    source = result.content
    soup = BeautifulSoup(source, 'lxml')
    base_stats_divs = soup.find("div", {"class": "grid-col span-md-12 span-lg-8"})
    tbody = base_stats_divs.find("tbody")
    total_th = base_stats_divs.find("tfoot").find_all("th")
    total_b = base_stats_divs.find("tfoot").findChildren("b")

    defenses = soup.find("div",{"resp-scroll text-center"})
    defenses_tables = defenses.find_all("table")
    origin_types = soup.find_all("table", {"class": "vitals-table"})[0].find_all("tr")[1].find_all("a")
    
    evolutions = soup.find("div", {"class": "infocard-list-evo"}).find_all("a", {"class": "ent-name"})
    evo_levels = soup.find("div", {"class": "infocard-list-evo"}).find_all("span", {"class": "infocard infocard-arrow"})

    
    try:    
        origin_types = [origin.text for origin in origin_types]
        base_stats["types"] = origin_types

        
        evo_levels = [int(evo_l.text.replace("(Level ", "").replace(")","")) for evo_l in evo_levels]
        evo_levels.insert(0,1)
        evolutions = [evo.text for evo in evolutions]
        
        levels = {}
        for lvl, evo in zip(evo_levels,evolutions):
            levels[lvl] = evo
        base_stats["levels"]  = levels

        ths = tbody.find_all('th')
        trs = tbody.find_all('tr')        
        for tr, th in zip(trs, ths):
            tds = tr.find_all("td")
            base_stats[th.text.lower().replace(".","_").replace(" ","")] = int(tds[0].text)
            base_stats["max_"+th.text.lower().replace(".","_").replace(" ","")] = int(tds[3].text)
            base_stats[total_th[0].text.lower()] = int(total_b[0].text)

        for table in defenses_tables:
            trs = table.find_all("tr")
            ths = trs[0].find_all("th")
            tds = trs[1].find_all("td")
            for th, td in zip(ths, tds):
                num = td.text.strip().replace("½", "0.5").replace("¼", "0.25")
                if num == "":
                    num = 1
                num = float(num)
                defense_stats[th.text.lower()+"_weakness"] = num

    except:
        pass
    stats = {}
    stats["base_stats"] = base_stats
    stats["defense_stats"] = defense_stats

    pokemons[name.capitalize()] = stats
    stats = {}

with open("data/pokemons.json", 'w') as f:
    json_object = json.dumps(pokemons, sort_keys=True, indent=4)
    f.write(json_object)

