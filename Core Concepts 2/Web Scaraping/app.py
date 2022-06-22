import requests
import pandas as pd
from bs4 import BeautifulSoup

# page = requests.get('https://forecast.weather.gov/MapClick.php?lat=34.053570000000036&lon=-118.24544999999995#.Yqv8kaJBxPY')
page = requests.get('https://forecast.weather.gov/MapClick.php?lat=41.8843&lon=-87.6324#.YqwNPqJBxPY')
soup = BeautifulSoup(page.content, 'html.parser')
# print(soup)

week = soup.find(id='seven-day-forecast-body')
# print(week)

items = week.find_all(class_='tombstone-container')
# print(items)

print(items[0].find(class_='period-name').get_text())
print(items[0].find(class_='short-desc').get_text())
print(items[0].find(class_='temp').get_text())

print()

print(items[4].find(class_='period-name').get_text())
print(items[4].find(class_='short-desc').get_text())
print(items[4].find(class_='temp').get_text())

print()

period_names = [item.find(class_='period-name').get_text() for item in items]
short_description = [item.find(class_='short-desc').get_text() for item in items]
temperatures = [item.find(class_='temp').get_text() for item in items]

print(period_names)
print(short_description)
print(temperatures)

whether_stuff = pd.DataFrame(
    {
    'period': period_names,
    'short_descriptions': short_description,
    'temperatures': temperatures
    }
)
print(whether_stuff)

whether_stuff.to_csv('weather2.csv')
print(whether_stuff)

print()