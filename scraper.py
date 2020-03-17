# -*- coding: utf-8 -*-
"""
Web scrapper to extract TV episodes names from IMDB
"""

import requests

#Variables
urlShow = 'https://www.imdb.com/title/tt1442437/episodes'	
urlInfo = 'season=4&ref_=tt_eps_sn_4'


url = urlShow + '?' + urlInfo