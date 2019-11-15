from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd


def web_scraper():

    # Request html and table from Wiki page

    source = requests.get('https://en.wikipedia.org/wiki/World_Happiness_Report').text
    soup = BeautifulSoup(source, 'lxml')
    # print(soup.prettify())

    ranking_table = soup.find('table', class_='wikitable sortable')

    table_rows = ranking_table.findAll('tr')
    row_list = []

    for tr in table_rows:
        td = tr.findAll('td')
        row = [i.text.replace('\n', ' ').strip() for i in td]
        row_list.append(row)
    return row_list

row_list = web_scraper()
# print(type(row_list))


ctry_dict = {}
for country in row_list:
    if len(country) > 0:
        ctry_dict[country[1]] = country[0]
# print(ctry_dict)
print(row_list)

# Iterate over list from scraper & create final list to include countries from
# World Happiness list only if they are in ctry_capitals.csv

Eur_data = []
ctryfile = 'ctry_capitals.csv'
new_list = []

with open(ctryfile) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for ctry in csv_reader:
        Country = ctry[1]
        if Country in ctry_dict:
            index = ctry_dict[Country]
            new_list = row_list[index]
            rank = new_list[0]
            info = {
                'Overall rank': rank,
                'Country or region',
                'Score',
                'GDP per capita',
                'Social support',
                'Healthy life expectancy',
                'Freedom to make life choices',
                'Generosity',
                'Perceptions of corruption'
            }
            Eur_data.append(info)


df = pd.DataFrame(Eur_data)
df.dropna(axis=0, how='any', inplace=True)
df.to_csv('world_happiness.csv', index=False)


# df = pd.DataFrame(row_list, columns=['Overall_rank', 'Country_or_Region', 'Score', 'GDP_per_capita',
#                                      'Social_support', 'Healthy_life_expectancy', 'Freedom_to_make_life_choices',
#                                      'Generosity', 'Perceptions_of_corruption'])
# print(df)