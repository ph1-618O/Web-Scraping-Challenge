#!/usr/bin/env python
# coding: utf-8

# # Mission to Mars
# - this program analyzes data from the NASA website

# # Dependencies

# In[1]:


import re
import pandas as pd
import numpy as np
import requests
import os
import json
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup as bs
from splinter import Browser
import time
from IPython.core.display import HTML
from datetime import date, datetime


# # Browser Assignment

# In[2]:


# fileName = input("Please enter the name of the file you'd like to use.")
# while not os.path.isfile(fileName):
#     fileName = input("Whoops! No such file! Please enter the name of the file you'd like to use.")


# In[3]:


get_ipython().system('which chromedriver')


# In[4]:


# # Open default browser to web page with Mac
# !python -m webbrowser -t "https://mars.nasa.gov/news/"


# In[5]:


#driver = webdriver.Chrome(executable_path='usr/local/bin/chromedriver')


# In[6]:


# Mac
# Choose the executable path to driver 
executable_path = {'executable_path': 'chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)


# In[7]:


# # PC
# # Choose the executable path to driver
#executable_path = {'executable_path': 'chromedriver.exe'}
#browser = Browser('chrome', **executable_path, headless=Fale)


# In[8]:


print(executable_path)


# # NASA Mars News
# Scrape the NASA Mars News Site and collect the latest News Title and Paragraph Text. Assign the text to variables that you can reference later.
# 
# #Example:
# news_title = "NASA's Next Mars Mission to Investigate Interior of Red Planet"
# 
# news_p = "Preparation of NASA's next spacecraft to Mars, InSight, has ramped up this summer, on course for launch next May from Vandenberg Air Force Base in central California -- the first interplanetary launch in history from America's West Coast."
def marsNewsScrape(url):
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)
    html = browser.html
    marsNewsSoup = bs(html, "html.parser")
    # newsLocation = marsNewsSoup.find_all("div", )
    #print(newsLocation)
    aSoup = marsNewsSoup.find_all('a')
    aSoup[0].attrs['href']
    for t in aSoup:
        print(t.text)

    #Getting the most recent headline
    headlineListN =[]
    recentHeadline = marsNewsSoup.find_all("div", attrs={'href'}, class_="content_title")
    for t in recentHeadline:
        headlineListN.append(t.text)
        #print(t.text)
    headlineList = []
    for i in headlineListN:
        headlineList.append(i.strip('\n'))
        #print(i.strip('\n'))
    return print(recentHeadline[0].text) print(headlineList)


# # Featured Image
# PL Mars Space Images - Featured Image
# Visit the url for JPL Featured Space Image here.
# https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars
# Use splinter to navigate the site and find the image url for the current Featured Mars Image and assign the url string to a variable called featured_image_url.
# Make sure to find the image url to the full size .jpg image.
# Make sure to save a complete url string for this image.
# #Example:
# featured_image_url = 'https://www.jpl.nasa.gov/spaceimages/images/largesize/PIA16225_hires.jpg'

def getMarsFeature(url):
    url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    response = requests.get(url)
    soup = bs(response.text, 'html.parser')
    print(soup.prettify())
    imagePartial = "https://www.jpl.nasa.gov"
    imageUrl = imagePartial + "/spaceimages/?search=&category=Mars"
    browser.visit(imageUrl)
    browser.click_link_by_partial_text('FULL IMAGE')
    expand = browser.find_by_css('a.fancybox-expand')
    imageSearch = browser.html
    imageSoup = bs(imageSearch, 'html.parser')
    results = imageSoup.find('img', {"class":"fancybox-image"})['src']
    fullImageLink = imagePartial + results
    #print(fullImageLink)
    return print(f'{imagePartial}{results}')
    #len(results)


def getMarsFacts(url):
    # # Mars Facts
    # Visit the Mars Facts webpage here and use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.
    # https://space-facts.com/mars/
    # Use Pandas to convert the data to a HTML table string.
    marsDataUrl = "https://space-facts.com/mars/"
    response = requests.get(marsDataUrl)
    soupResponse = bs(response.text, 'html.parser')
    #print(soupResponse.prettify())
    browser.visit(marsDataUrl)
    marsDataSearch = browser.html
    marsDataSoup = bs(marsDataSearch, 'html.parser')    
    #Printing response as string to analyze
    strMars = str(marsDataSoup.find_all())
    print(type(strMars))
    htmlStringLength = len(strMars)
    print(type(htmlStringLength))
    print(htmlStringLength)
    partialHTML = int(htmlStringLength * .10/100)
    print(strMars[:partialHTML])
    #Writing response to HTML file to view
    htmlFile = open("response.html", "w")
    htmlFile .write(strMars)
    htmlFile.close()


    browser.visit(marsDataUrl)
    marsDataSearch = browser.html
    marsDataSoup = bs(marsDataSearch, 'html.parser')
    results = marsDataSoup.find('table', {"class":"tablepress"})
    marsList = pd.read_html(marsDataUrl)
    print(type(marsList))
    # print(marsList)
    marsDict = dict(marsList[1])
    marsComparisonDF = pd.DataFrame.from_dict(marsDict)
    #print(type(marsComparisonDF))
    #marsComparisonDF
    marsDict = dict(marsList[0])
    #marsDict[1]
    marsDF = pd.DataFrame.from_dict(marsDict)
    print(type(marsDF))
    marsDF = marsDF.rename(columns = {0: "Measurement", 1:"Value"})
    #marsDF

# # Mars Hemispheres
def hemisphereData(hemisphereUrl):
# 
# Visit the USGS Astrogeology site here to obtain high resolution images for each of Mar's hemispheres.
# https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars
# Click each of the links to the hemispheres to find the image url to the full resolution image.
# Save both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name. Use a Python dictionary to store the data using the keys img_url and title.
# Append the dictionary with the image url string and the hemisphere title to a list. This list will contain one dictionary for each hemisphere.
# 
# #Example:
# hemisphere_image_urls = [
#     {"title": "Valles Marineris Hemisphere", "img_url": "..."},
#     {"title": "Cerberus Hemisphere", "img_url": "..."},
#     {"title": "Schiaparelli Hemisphere", "img_url": "..."},
#     {"title": "Syrtis Major Hemisphere", "img_url": "..."},

# hemiURL = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
# browser.visit(hemiURL)
# hemiSearch = browser.html
# hemiSoup = bs(hemiSearch, 'html.parser')

# browser.click_link_by_partial_text('FULL IMAGE')
# expand = browser.find_by_css('a.fancybox-expand')

# imageSearch = browser.html
# imageSoup = bs(imageSearch, 'html.parser')
# results = imageSoup.find('img', {"class":"fancybox-image"})['src']

    hemisphereDicts = {"Reason":"Website down unable to scrape"}


# # FLASK APPLICATION/ MONGO DB
# Use MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.
marsCompareDict = marsComparisonDF.to_dict()
marsCompareDict
marsDict = marsDF.to_dict()
marsDict
exportDict = {
    "headlines": headlineList, 
    "imageLink": fullImageLink, 
    "DF1": marsDict, 
    "DF2": marsCompareDict, 
    "hemi": hemisphereDicts}

#exportDict


#installing jupyter notebook converter
get_ipython().system('pip install nbconvert')
#conda install nbconvert
#converting ipynb to py
get_ipython().system('jupyter nbconvert --to python webScraping.ipynb')
#renaming ipynb to scrape_mars.py
get_ipython().system('mv webScraping.py scrape_mars.py')
get_ipython().run_line_magic('load', 'scrape_mars.py')
#!/usr/bin/env python

# # Mission to Mars
# - this program analyzes data from the NASA website




