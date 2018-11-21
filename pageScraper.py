import csv
import requests
from bs4 import BeautifulSoup

#NEXT STEPS: how are you going to save the data in a relational way with a key that makes it findable and accessible. Different case than quick stats because these will change and the keys aren't updated all at once.

url = 'https://awoiaf.westeros.org/index.php/Jaime_Lannister'
response = requests.get(url)
html = response.content

targets = []

soup = BeautifulSoup(html, "html.parser")
name = soup.select_one('#firstHeading')

targets.append(name)

startingElement = soup.select_one('.infobox')

for sibling in startingElement.next_siblings:
	if sibling.name == 'div':
		break
	targets.append(sibling)

print(targets)

# outfile = open("./linksTwo.csv", "w", newline='')
# writer = csv.writer(outfile)

# # writer.writerow(["Player", "Pos", "Age", "Tm", "G", "GS", "MP", "FG", "FGA", "FG%", "3P", "3PA", "3P%", "2P", "2PA", "2P%", "eFG%", "FT", "FTA", "FT%", "ORB", "DRB", "TRB", "AST", "STL", "BLK", "TOV", "PF", "PS/G"])
# writer.writerows(map(lambda x: [x], list_of_rows))




