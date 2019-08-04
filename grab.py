#!/usr/bin/python2

import urllib2
import re

urlShell = "https://projecteuler.net/problem="

for i in range(1,667):
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
