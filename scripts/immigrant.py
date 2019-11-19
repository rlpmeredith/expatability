from bs4 import BeautifulSoup
import requests
import pandas as pd
import csv
import lxml


def scrape_page():

    # Request page from Gallup.com and get table

    url = 'https://news.gallup.com/poll/216377/new-index-shows-least-accepting-countries-migrants.aspx'
    source = requests.get(url)
    soup = BeautifulSoup(source.content, 'lxml')
    tables = soup.find_all('table', attrs={'class':'mobile'})
    my_table = tables[4]

    # Get data from each row in table

    rows = my_table.find_all("tr")
    data = {}

    for row in rows:
        country = row.find('th')
        result = row.find('td')
        if country and result and country.text != " " and result.text != " ":
            data[country.text] = result.text
    return data


data = scrape_page()
immigrant_data = []
cityfile = "../data/ctry_capitals.csv"

with open(cityfile) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for city in csv_reader:
        country = city[0]
        if country in data:
            info = {
            "country": country,
            "index": data[country]
            }
            immigrant_data.append(info)

df = pd.DataFrame(immigrant_data)
immigrant_data = '../data/immigrant.csv'
df.to_csv(immigrant_data, index=False )