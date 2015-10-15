
# coding: utf-8
import os
import requests
from bs4 import BeautifulSoup as bs
from bs4 import SoupStrainer
import csv
import datetime


###Get a list of URLs
########################################

outputpath = os.path.abspath(os.path.join(os.path.dirname('__file__'), '..', 'Output'))
outputfile = os.path.join(outputpath, "URL list albums.csv")

print datetime.datetime.now()

for pagenum in range(1, 4800):
    #Create tracking markers
    if not (pagenum % 500):
        print pagenum
    
    #This will scrape all albums
    url = 'http://imgur.com/search/time/all/page/'+ str(pagenum)+'?scrolled&q_size_is_mpx=off&q_any=anigif,%20gif,%20png,%20jpg&q_type=album'
    #Get URL results
    results = requests.get(url).text

    #Soupeify it!
    soup = bs(results, 'html.parser')

    #Parse out hyperlinks
    url_list = []
    for link in bs(results, parse_only=SoupStrainer('a')):
        if link.has_attr('href') and link['href'] != 'javascript:;':
            fileid = link['href'].replace('/gallery/', '')
            url_list.append(fileid)

    #Write results to a file
    for u in url_list:
        with open(outputfile, "ab") as myfile:
            filewriter = csv.writer(myfile)
            filewriter.writerow([u, 'jpg'])
            
print datetime.datetime.now()            



