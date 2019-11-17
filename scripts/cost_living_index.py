from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd


def web_scraper():

    source = requests.get('https://www.expatistan.com/cost-of-living/index/europe')
    # print(source.status_code)

    soup = BeautifulSoup(source.content, 'lxml')

    cost_table = soup.find('table', class_='city-index')
    rows = cost_table.findAll('tr')

    row_list = []

    for row in rows:
        info = row.findAll('td')
        row = [i.text.replace('\n', ' ').strip() for i in info]
        row_list.append(row)


# Create new list of city-country strings to iterate over string & remove country, then put back in list
# with the rank and price index

    city_list = []
    for x in row_list:
        if len(x) > 0:
            city_name = x[1]
            city_str = city_name.split('(')[0]
            city_str = city_str.replace(' ', '')
            # print(city_str)

            new_list = [x[0], city_str, x[2]]
            city_list.append(new_list)
    return(city_list)



def city_pages(city):

    # for city in cities
    # call ctry_pages fn for each city
    url = f'https://www.expatistan.com/cost-of-living/{city}'
    source = requests.get(url)
    if source.status_code == 200:


        soup = BeautifulSoup(source.content, 'lxml')

        cost_table = soup.find('table', class_='comparison single-city')
        # print(type(cost_table))

        rows = cost_table.findAll('tr')
        row_list = []

        for tr in rows:
            td = tr.findAll('td')
            row = [i.text.replace('\n', ' ').strip() for i in td]
            if len(row) > 1:
                if row[1] == 'Basic lunchtime menu (including a drink) in the business district':
                    new_list = ['Lunchtime_menu', row[2]]
                    row_list.append(new_list)

                elif row[1] == 'Monthly rent for 85 m2 (900 Sqft) furnished accommodation in NORMAL area':
                    new_list = ['Monthly_rent', row[2]]
                    row_list.append(new_list)

                elif row[1] == 'Monthly ticket public transport':
                    new_list = ['Public_transport_month', row[2]]
                    row_list.append(new_list)

        return(row_list)
    return



data = web_scraper()
# print(data)
cost_data = []
src_file = "../data/ctry_capitals.csv"

with open(src_file) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for capital in csv_reader:
        name = capital[3]
        name = name.replace(" ", "-")
        print(name)

        if name and name != 'Capital':

            print('calling function')
            capital_data = city_pages(name.lower())
            if capital_data:
                lunchtime_menu = capital_data[0][1]
                monthly_rent = capital_data[1][1]
                public_trans = capital_data[2][1]

                print(public_trans)

                for x in data:
                    if name == x[1]:
                        print('matched')
                        index = x[2]
                        rank = x[0]

                        # print(name, index, rank, lunchtime_menu, monthly_rent, public_trans)

                        info = {
                            "Capital": name,
                            "Price_index": index,
                            "Rank": rank,
                            "Lunch": lunchtime_menu,
                            "Rent": monthly_rent,
                            "Public_trans": public_trans
                            }
                        cost_data.append(info)


df = pd.DataFrame(cost_data)
df.dropna(axis=0, how='any', inplace=True)
df.to_csv('../data/cost_living_index.csv', index=False)