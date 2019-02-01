import os.path
import requests
from bs4 import BeautifulSoup
import time

# import array of characters  
from characterArray import *

for person in characters:
	time.sleep(2)
	url = 'https://awoiaf.westeros.org/index.php/' + person
	try:
		response = requests.get(url)
		html = response.content
		save_path = "/Users/alexrichards/Code/Projects/GOT-Finder/character_html_files"
		file_name = person

		complete_path = os.path.join(save_path, file_name + ".html")

		file = open(complete_path, 'wb')
		file.write(html)
		file.close()
	except requests.exceptions.RequestException as e:
		print(e, person)
		pass




#### For scraping individual pages for the character summary heading ####
# targets = []

# soup = BeautifulSoup(html, "html.parser")
# name = soup.select_one('#firstHeading')

# targets.append(name)

# startingElement = soup.select_one('.infobox')

# for sibling in startingElement.next_siblings:
# 	if sibling.name == 'div':
# 		break
# 	targets.append(sibling)





