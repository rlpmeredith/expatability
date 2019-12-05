from bs4 import BeautifulSoup
import requests
import pandas as pd
from unidecode import unidecode


# REQUEST HTML AS TEXT FROM WIKIPEDIA SITE

source = requests.get('https://simple.wikipedia.org/wiki/List_of_European_countries').text
soup = BeautifulSoup(source, 'lxml')

# USE BEAUTIFULSOUP TO EXTRACT THE TABLE

ctry_table = soup.find('table', class_='wikitable sortable references-small')


#  REMOVE ALL SPAN AND SUP TAGS WHICH CORRESPOND TO REFERENCES/NOTES

for tag in ctry_table.findAll(['span', 'sup']):
    tag.decompose()

table_rows = ctry_table.findAll('tr')
row_list = []

for tr in table_rows:
        td = tr.findAll('td')
        row = [i.text.replace('\n', ' ').strip() for i in td if i != '']
        row_list.append(row)
        row_list = list(filter(None, row_list))

# Create dataframe with Pandas and specify new column names, remove unwanted columns and clean data

df = pd.DataFrame(row_list, columns=['Country_or_Territory', 'Area', 'Population', 'Pop_density', 'Capital'])
df.dropna(axis=0, how='any', inplace=True)
df.drop(['Area', 'Pop_density'], axis=1, inplace=True)
df['Population'] = df['Population'].str.replace(',', '')
df['Population'] = df['Population'].apply(pd.to_numeric, errors='coerce')

df['Capital'] = df['Capital'].apply(unidecode)

df.to_csv('../data/ctry_capitals.csv', index=False)
