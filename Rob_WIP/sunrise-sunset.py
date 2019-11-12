import requests
import csv


# Start with simple list of cities

with open('../data/citylist.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0

# Function to get lat/long from opencagedata


def get_latlong(city):

    print(city)
    # cityname = city[0]
    url = f"https://api.opencagedata.com/geocode/v1/json?q={city}&key=054d264611394f699a5a1d5e16ba3cb1"
    response = requests.get(url)
    j = response.json()
    print(response.status_code)
    if response.status_code == 200:
        lat = j['results']['geometry']['lat']
        long = j['results']['geometry']['long']

    return lat, long


lat, long = get_latlong("London")
print(lat)
print(long)



