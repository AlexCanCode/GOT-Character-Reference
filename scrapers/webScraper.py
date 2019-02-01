import csv
import requests
from bs4 import BeautifulSoup

url = 'https://awoiaf.westeros.org/index.php/List_of_characters'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html, "html.parser")
table = soup.select_one('.mw-parser-output')

list_of_rows = []
for row in soup.find_all('a'):
	list_of_cells = []
	list_of_rows.append(row.get('href'))

# set_of_links = list(set(list_of_rows))
# print(set_of_links)

# clean_list_of_rows = filter(None, list_of_rows)

outfile = open("./linksTwo.csv", "w", newline='')
writer = csv.writer(outfile)

# writer.writerow(["Player", "Pos", "Age", "Tm", "G", "GS", "MP", "FG", "FGA", "FG%", "3P", "3PA", "3P%", "2P", "2PA", "2P%", "eFG%", "FT", "FTA", "FT%", "ORB", "DRB", "TRB", "AST", "STL", "BLK", "TOV", "PF", "PS/G"])
writer.writerows(map(lambda x: [x], list_of_rows))




