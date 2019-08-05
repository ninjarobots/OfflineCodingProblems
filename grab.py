#!/usr/bin/python2

from BeautifulSoup import BeautifulSoup
import urllib2
import re

import os
import errno

urlShell = "https://projecteuler.net/problem="
base = "https://projecteuler.net/"

def getLinks(html_page):
    #html_page = urllib2.urlopen(url)
    soup = BeautifulSoup(html_page)
    links = []

    for link in soup.findAll('a', attrs={'href': re.compile(r'\w+\.(txt|png|jpg|jpeg)')}):
        links.append(link.get('href'))

    return links

def saveFile(url, base, directory):
    response = urllib2.urlopen(base + url)
    text = str(response.read())
    filename = directory + url
    if not os.path.exists(os.path.dirname(filename)):
        try:
            os.makedirs(os.path.dirname(filename))
        except OSError as exc: # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise

    with open(filename, "w") as f:
        file.write(text)

    return


for i in [96]:
    url = (urlShell + str(i))
    response = urllib2.urlopen(url)
    text = str(response.read())
    fileName = re.search ("<h2>"r".*""</h2>", text)
    fn = fileName.group().strip("<h2>")
    fn = fn.strip("</")
    fn = fn.replace(" ", "_")
    fn = "exercises/" + str(i) + "." + fn + ".html"
    print(fn)
    file = open(fn, "w")
    file.write(text)
    file.close
    links =  getLinks(text) 
    print links
    for link in links:
        saveFile(link, base, "exercises/")

