# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 15:19:10 2020

@author: Gerardo

Script uses data sraped from scraper to 
rename files on specified directory
"""

import os
import string
from scraper import imdbScraper

#TODO: check seaon indexes are givern in right order
s = imdbScraper('https://www.imdb.com/title/tt1442437/episodes',11,12)
#print(s.getData())


path = r'C:\Users\Gerardo\Personal\Media\Shows\Modern Family\Season 11'
filePrefix = 'Modern Family S'
#Valid chars to use in file names
validChars = "-_.,()&!' %s%s" % (string.ascii_letters, string.digits)
titles = s.getData()

i = 0
for filename in os.listdir(path):
    print(os.path.isdir(filename))
    print(filename)
    #TODO: check indexError whenthere is a directory inside the folder
    if not os.path.isdir(filename):
        #Creates file name  with specified prefix, and removes unwanted characters from the data downloaded
        newName = filePrefix + ''.join(c for c in titles[i] if c in validChars)
        oldName = filename
        filename , fileExtension = os.path.splitext(filename)       
        
        # dst = path + "\\" + dst 
        #print(fileExtension)  
        
        # # rename() function will 
        # # rename all the files 
        #os.rename( path + "\\" + oldName, path + "\\" + newName + fileExtension) 
        print("Rename file " + oldName + " to " + newName + fileExtension + " ?")
        i += 1