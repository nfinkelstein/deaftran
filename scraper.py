import urllib
import urllib2
#import requests
import imageio
import re
import csv
import os
imageio.plugins.ffmpeg.download()


mike_path = "C:\\Users\\mikeb\\Documents\\GitHub\\deaftran\\static\\"
nico_path = "/Users/nico/Desktop/hackillinois/static/"

mike_short_path = "static\\"
nico_short_path = "static/"

curr_OS = 'nico'


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

    for each in terms:
        re.sub(r'[^\w]', '', each)

    return terms

def generate_gifs(terms):

    mydict = get_dict_from_csv("./real_outputs.csv")
    i = 1
    for term in terms:
        term = term.lower()


        if term in mydict:

            print("Generating gif for", term)

            url = 'https://www.handspeak.com/word/' + term[0] + '/' + term + '.mp4'
            print(url)
            headers = {'User-Agent': 'Mozilla/5.0'}
            video_req = urllib.FancyURLopener()
            video_req.retrieve(url, "video.mp4")

            clip = (VideoFileClip("video.mp4"))

            if curr_OS == 'mike':
                clip.write_gif(mike_short_path + str(i) + '-' + term + "-asl.gif")
            elif curr_OS == 'nico':
                clip.write_gif(nico_short_path + str(i) + '-' + term + "-asl.gif")

            i = i + 1


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
    str = raw_input('Type sentence to translate: ')
    terms = parse_input(str)
    generate_gifs(terms)

__main__()