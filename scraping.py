from bs4 import BeautifulSoup
import requests
import pandas as pd

start_url = 'https://en.wikipedia.org/wiki/List_of_brown_dwarfs'
webpage = requests.get(start_url)
soup = BeautifulSoup(webpage.text, "html.parser")

star_table_find = soup.find_all('table')
print(len(star_table_find))

temp_list = []

table_rows = star_table_find[7].find_all("tr")
for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)
print(temp_list)

star_names = []
distance = []
mass = []
radius = []

for i in range(1, len(temp_list)):
    star_names.append(temp_list[i][0])
    distance.append(temp_list[i][5])
    mass.append(temp_list[i][7])
    radius.append(temp_list[i][8])

dataframe2 = pd.DataFrame(list(zip(star_names, distance, mass, radius)), columns=[
                          "Name of Star", "Distance (in ly)", "Mass", "Radius"])
print(dataframe2)

dataframe2.to_csv("dwaft_stars.csv")
