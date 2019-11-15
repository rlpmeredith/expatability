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

# Run function to scrape page

row_list = web_scraper()

# Create dictionary from list so we have dict of Countries from page

country_dict = {}
for country in row_list:
    if len(country) > 0:
        country_dict[country[1]] = country[0]

# Iterate over list from scraper & create final list to include countries from
# World Happiness list only if they are in ctry_capitals.csv

happiness_data = []
countryfile = '../data/ctry_capitals.csv'
new_list = []
info = {}

with open(countryfile) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for country in csv_reader:
        country_name = country[1]
        if country_name in country_dict:
            index = int(country_dict[country_name])
            info = {
                'Rank': row_list[index][0],
                'Country': row_list[index][1],
                'Score': row_list[index][2],
                'GDP per capita': row_list[index][3],
                'Social support': row_list[index][4],
                'Healthy life expectancy': row_list[index][5],
                'Freedom to make life choices': row_list[index][6],
                'Generosity': row_list[index][7],
                'Perceptions of corruption': row_list[index][8],
            }
            happiness_data.append(info)


df = pd.DataFrame(happiness_data)
df.dropna(axis=0, how='any', inplace=True)
df.to_csv('../data/world_happiness.csv', index=False)


# df = pd.DataFrame(row_list, columns=['Overall_rank', 'Country_or_Region', 'Score', 'GDP_per_capita',
#                                      'Social_support', 'Healthy_life_expectancy', 'Freedom_to_make_life_choices',
#                                      'Generosity', 'Perceptions_of_corruption'])
# print(df)