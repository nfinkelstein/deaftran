import urllib
import urllib2
import requests
import imageio
import re

dict = {}

for i in range(1,2):
    url = 'https://www.handspeak.com/word/search/index.php?id=' + str(i)
    headers = {'User-Agent' : 'Mozilla/5.0'}
    response = urllib2.urlopen(url, None, headers)
    html = response.read()



print(html)

