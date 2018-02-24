import bs4
from urllib.request import urlopen
from bs4 import BeautifulSoup as soup

url = "https://www.handspeak.com/word/"

uClient = urlopen(url)

page_html = uClient.read()

uClient.close()

page_soup = soup(page_html, "html.parser")

# grabs each word
containers = page_soup.findAll("a")

print(len(containers))
