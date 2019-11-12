import requests
import csv
import pprint
import pandas as pd



def get_latlong(city):

    # Function to get lat/long from opencagedata

    url = f'https://api.opencagedata.com/geocode/v1/json?q={city}&key=054d264611394f699a5a1d5e16ba3cb1'
    response = requests.get(url)
    j = response.json()
    if response.status_code == 200:
        latitude = j['results'][0]['geometry']['lat']
        longitude = j['results'][0]['geometry']['lng']

    return latitude, longitude


def get_shortest_longest_day(latitude, longitude):

    # Function to get shortest and longest day lengths from sunrise-sunset

    shortest_day = '2020/12/21'
    longest_day = '2020/06/20'
    shortest_url = f'https://api.sunrise-sunset.org/json?lat={latitude}&lng={longitude}&date={shortest_day}'
    longest_url = f'https://api.sunrise-sunset.org/json?lat={latitude}&lng={longitude}&date={longest_day}'
    shortest_response = requests.get(shortest_url)
    j_shortest_response = shortest_response.json()
    longest_response = requests.get(longest_url)
    j_longest_response = longest_response.json()

    if shortest_response.status_code == 200:
        shortest_day_length = j_shortest_response['results']['day_length']
    if longest_response.status_code == 200:
        longest_day_length = j_longest_response['results']['day_length']

    return shortest_day_length, longest_day_length


# Start with simple list of cities

cityfile = '../data/citylist.csv'
daydata = '../data/daydata.csv'
citydata = []

with open(cityfile) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for city in csv_reader:
        lat, lng = get_latlong(city[0])
        short, long = get_shortest_longest_day(lat, lng)
        info = {
            "city": city[0],
            "lat": lat,
            "lng": lng,
            "shortest_day": short,
            "longest_day": long
        }
        citydata.append(info)
    df = pd.DataFrame(citydata)

df.to_csv(daydata, index=False)


