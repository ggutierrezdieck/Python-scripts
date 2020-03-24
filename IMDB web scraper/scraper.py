# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 15:19:10 2020

@author: Gerardo

Web scrapper to extract TV episodes names from IMDB
"""

import requests
from bs4 import BeautifulSoup



class imdbScraper(object):
    def __init__(self, urlShow, fS = 1, lS =11):
        #Variables
        #urlShow = 'https://www.imdb.com/title/tt1442437/episodes'
        self.urlShow = urlShow
        self.firstSeason = fS
        self.lastSeason = lS
        
    def getData(self):
        episodeTitle = []
        for i in range(self.firstSeason,self.lastSeason,1):
            urlInfo = 'season=' + str(i) + '&ref_=tt_eps_sn_' + str(i) 
            
            #TODO: hanlde exceptions
            url = self.urlShow + '?' + urlInfo
            page = requests.get(url)
            soup = BeautifulSoup(page.content, 'html.parser')
            results = soup.find('div',class_="list detail eplist")
            episodes = results.find_all('div',itemprop="episodes")
            for episode in episodes:
                ''''print('Modern Family s' + str(i).zfill(2) + 'e' +
                      episode.find('meta')['content'].zfill(2) + ' - ' + 
                      episode.find('a')['title'])'''
                #print(results.prettify())
                episodeTitle.append(str(i).zfill(2) + 'e' + 
                                    episode.find('meta')['content'].zfill(2) + ' - ' + 
                                    episode.find('a')['title'])
        return episodeTitle
    
    
