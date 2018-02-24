# import urllib
# import urllib2
# import requests
# import imageio
import re

from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
import csv

mydict = {}
idnum = 1

for i in range(5000,7650):

	try:
		url = 'https://www.handspeak.com/word/search/index.php?id=' + str(i)

		uClient = urlopen(url)
		page_html = uClient.read()
		uClient.close()

		page_soup = soup(page_html, "html.parser")

		word = ""
		vidlink = ""

		word = page_soup.video["title"][13:] #get rid of "asl sign for "
		vidlink = "https://www.handspeak.com" + page_soup.video["src"]

		mydict[word] = vidlink

	except: print("Error in id number ", idnum)



w = csv.writer(open("real_outputs3.csv", "w")) # write to CSV
for key in mydict.keys():
    w.writerow([key, mydict[key]])




