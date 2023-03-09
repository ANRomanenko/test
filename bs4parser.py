# Load in the necessary libraies

import requests # pip install requests
from bs4 import BeautifulSoup as bs # pip install beautifoulsoup4

# Load our first page
# Load the webpage content

r = requests.get("https://keithgalli.github.io/web-scraping/example.html")

# Convert to a beautifulsoup object

soup = bs(r.content)

# Print out our html

print(soup.prettify())

# Start using Beautiful Soup to Scrape
# find and find_all

first_header = soup.find("h2")
print(first_header)

header = soup.find_all("h2")
print(header)

# Pass in a list of elements to look for

first_header = soup.find(["h1", "h2"])
print(first_header)

headers = soup.find_all(["h1", "h2"])
print(headers)

# You can pass in attributes to the find/find_all function

paragraph = soup.find_all("p", attrs={"id": "paragraph-id"})
print(paragraph)
print()

# You can nest find/find_all calls

body = soup.find("body")
print(body)
print()
div = body.find("div")
print(div)
print()
header = div.find('h1')
print(header)
print()
# We can search specific strings in our find/find_all calls

paragraph = soup.find_all("p", string="Some bold text")
print(paragraph)
