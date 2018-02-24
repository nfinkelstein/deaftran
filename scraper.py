import urllib
#import urllib2
#import requests
#import imageio
import re
import csv
#from moviepy.editor import *


ignore_list = ('a','am','the')

def parse_input(str):

    terms = str.split(' ')

    for each in terms:
        re.sub(r'[^\w]', '', each)

    return terms

def generate_gifs(terms):
    mydict = get_dict_from_csv("./real_outputs.csv")
    for term in terms:
        term = term.lower()

        if term in mydict:
            print("Generating gif for", term)

def get_dict_from_csv(csvfile):
    reader = csv.reader(open(csvfile, 'r'))
    d = {}
    for row in reader:
        k = row[0]
        v = row[1]
        d[k] = v
    return d

def __main__():
    str = input('Type sentence to translate: ')
    terms = parse_input(str)
    generate_gifs(terms)

__main__()