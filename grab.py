#!/usr/bin/python2

from BeautifulSoup import BeautifulSoup
import urllib2
import re

urlShell = "https://projecteuler.net/problem="

def getLinks(html_page):
    #html_page = urllib2.urlopen(url)
    soup = BeautifulSoup(html_page)
    links = []

    for link in soup.findAll('a'):
        links.append(link.get('href'))

    return links



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
    print( getLinks(text) )

