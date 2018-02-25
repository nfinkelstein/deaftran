import urllib
import urllib2
#import requests
import imageio
import re
import csv
import os
from moviepy.editor import *
from nltk.stem.lancaster import LancasterStemmer


mike_path = "C:\\Users\\mikeb\\Documents\\GitHub\\deaftran\\static\\gifs\\"
nico_path = "/Users/nico/Desktop/hackillinois/static/gifs/"

mike_short_path = "static\\gifs\\"
nico_short_path = "static/gifs"

curr_OS = 'mike'


def clear_GIFS_directory():

    if curr_OS == 'mike':
        for the_file in os.listdir(mike_path):
            file_path = os.path.join(mike_path, the_file)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)

            except Exception as e:
                print(e)

    elif curr_OS == 'nico':
        for the_file in os.listdir(nico_path):
            file_path = os.path.join(nico_path, the_file)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)

            except Exception as e:
                print(e)


def parse_input(str):

    terms = str.split(' ')

    i = 0
    for each in terms:
        terms[i] = re.sub(r'[\W]', '', each)
        #re.sub(r'.', '', each)
        print(each)
        i = i + 1

    return terms

def generate_gifs(terms):

    gifs = list();
    mydict = get_dict_from_csv("./real_outputs.csv")

    for term in terms:
        term = term.lower()


        if term == "men":
            term = "man"
        elif term == "women":
            term = "woman"

        st = LancasterStemmer()
        if term not in mydict: term = st.stem(term)

        if term in mydict:

            #print("Generating gif for", term)

            url = mydict[term]

            #print(url)

            headers = {'User-Agent': 'Mozilla/5.0'}
            video_req = urllib.FancyURLopener()
            video_req.retrieve(url, "video.mp4")

            clip = (VideoFileClip("video.mp4"))
            clip = clip.resize(width=320)
            clip = clip.resize(height=240)

            if curr_OS == 'mike':
                clip.write_gif(mike_short_path + term + "-asl.gif")
                gifs.append(term + "-asl.gif")
            elif curr_OS == 'nico':
                clip.write_gif(nico_short_path + term + "-asl.gif")
                gifs.append(term + "-asl.gif")

    return gifs


def get_dict_from_csv(csvfile):
    reader = csv.reader(open(csvfile, 'r'))
    d = {}
    for row in reader:
        k = row[0]
        v = row[1]
        d[k] = v
    return d

def __main__():

    clear_GIFS_directory()
    #str = raw_input('Type sentence to translate: ')
    #terms = parse_input(str)
    #gifs = generate_gifs(terms)

__main__()