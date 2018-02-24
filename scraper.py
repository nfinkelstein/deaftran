import urllib
import urllib2
import requests
import imageio
import re
from moviepy.editor import *


ignore_list = ('a','am','the')

def parse_input(str):

    terms = str.split(' ')

    for each in terms:
        re.sub(r'[^\w]', '', each)

    return terms

def generate_gifs(terms):

    i = 1
    for term in terms:
        term = term.lower()

        if(term == "i"):
            term = "me"

        if (term == "dog"):
            term = "dog-fs"

        if(term in ignore_list):
            continue

        url = 'https://www.handspeak.com/word/'+ term[0] +'/' + term + '.mp4'
        print(url)
        headers = {'User-Agent' : 'Mozilla/5.0'}
        video_req=urllib.FancyURLopener()
        video_req.retrieve(url,"video.mp4")


        clip = (VideoFileClip("video.mp4"))
        clip.write_gif(str(i) + '-' + term + "-asl.gif")

        i = i + 1

def __main__():
    str = raw_input('Type sentence to translate: ')
    terms = parse_input(str)
    generate_gifs(terms)

__main__()