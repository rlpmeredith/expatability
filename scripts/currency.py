from bs4 import BeautifulSoup
import requests
import pandas as pd

# Request HTML as text from XE site

my_url = 'https://www.xe.com/symbols.php'
source = requests.get(my_url).text

soup = BeautifulSoup(source, 'lxml')


# Use BS to extract the table

currency_table = soup.find('table', class_='currencySymblTable')

table_rows = currency_table.findAll('tr')

row_list = []

for tr in table_rows:
    td = tr.findAll('td')
    row = [i.text.replace('\n', ' ').strip() for i in td if i != '']
    row_list.append(row)
    row_list = list(filter(None, row_list))
# print(row_list)


# Create dataframe with Pandas and specify new column names, remove unwanted columns and clean data


df = pd.DataFrame(row_list, columns=['Country_and_Currency', 'Code', 'Image', 'Font: Code2000', 'Currency_Symbol'
                                     'Font: Unicode MS', 'Unicode: Decimal', 'Unicode: Hex', ''])
df.drop(['Code', 'Image', 'Font: Code2000', 'Unicode: Decimal', 'Unicode: Hex', ''], axis=1, inplace=True)
df.dropna(axis=0, how='any', inplace=True)
df.to_csv('../data/currency.csv', index=False)

df.to_csv('../data/currency.csv', header=None, index=False)


# df.rename(columns={'Country_and_Currency': 'Country and Currency', 'Currency_Symbol': 'Font: Arial Unicode MS'}, inplace=True)
