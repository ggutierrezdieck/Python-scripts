# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 15:19:10 2020

@author: Gerardo

Script uses data sraped from scraper to 
rename files on specified directory
"""

from scraper import imdbScraper

s = imdbScraper('https://www.imdb.com/title/tt1442437/episodes',4,5)
print(s.getData())

