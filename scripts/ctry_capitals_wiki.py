from bs4 import BeautifulSoup
import requests
import pandas as pd


# REQUEST HTML AS TEXT FROM WIKIPEDIA SITE

source = requests.get('https://simple.wikipedia.org/wiki/List_of_European_countries').text
soup = BeautifulSoup(source, 'lxml')
# print(soup.prettify())

# USE BEAUTIFULSOUP TO EXTRACT THE TABLE

ctry_table = soup.find('table', class_='wikitable sortable references-small')


#  REMOVE ALL SPAN AND SUP TAGS WHICH CORRESPOND TO REFERENCES/NOTES

for tag in ctry_table.findAll(['span', 'sup']):
    tag.decompose()

table_rows = ctry_table.findAll('tr')
row_list = []

for tr in table_rows:
    td = tr.findAll('td')
    row = [i.text.replace('\n', ' ').strip() for i in td]
    row_list.append(row)
# print(row_list)


# CREATE DATAFRAME WITH PANDAS AND SPECIFY NEW COLUMN NAMES, REMOVE UNWANTED COLUMNS

df = pd.DataFrame(row_list, columns=['Country_or_Territory', 'Area', 'Population', 'Pop_density', 'Capital'])
# print(df)
df.dropna(axis=0, how='any', inplace=True)
df.drop(['Area', 'Pop_density'], axis=1, inplace=True)

df.to_csv('../data/ctry_capitals.csv', index=False)
