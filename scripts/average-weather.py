import requests
import csv
import pprint
import pandas as pd
from bs4 import BeautifulSoup
import re

def average_weather(city):

    # Scrape January Page from Holiday Weather
    # Parse with BS

    # Replace spaces with underscores

    city = city.replace(" ", "_")
    print(city)

    url = f'https://www.holiday-weather.com/{city}/averages/january'
    page = requests.get(url)
    print(page.status_code)
    soup = BeautifulSoup(page.content, 'html.parser')
    div = soup.find("div", attrs={"class": "panel panel--no-padding", "id": "averages_info"})

    # Find avg temp for January

    if div:
        line = div.find_all(class_="destination-info__details")
        firstresult = line[0].text
        jan_avg_temp = firstresult.split('C')[0]
        jan_avg_temp = jan_avg_temp.replace(u'\N{DEGREE SIGN}', '')

    else:
        return None, None

    # Scrape July Page from Holiday Weather
    # Parse with BS

    url = f'https://www.holiday-weather.com/{city}/averages/july'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    div = soup.find("div", attrs={"class": "panel panel--no-padding", "id": "averages_info"})
    line = div.find_all(class_="destination-info__details")

    # Find avg temp for July

    firstresult = line[0].text
    july_avg_temp = firstresult.split('C')[0]
    july_avg_temp = july_avg_temp.replace(u'\N{DEGREE SIGN}', '')

    return jan_avg_temp, july_avg_temp

cityfile = '../data/citylist.csv'
tempdata = '../data/tempdata.csv'
data = []

with open(cityfile) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for city in csv_reader:
        print(city)
        jan, july = average_weather(city[0])
        info = {
            "city": city[0],
            "jan_avg": jan,
            "jul_avg": july,
        }
        data.append(info)
    df = pd.DataFrame(data)

df.to_csv(tempdata, index=False)