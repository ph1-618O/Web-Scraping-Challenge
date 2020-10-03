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
def marsNewsScrape():
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
    print(recentHeadline[0].text)
    for t in recentHeadline:
        headlineListN.append(t.text)
        #print(t.text)
    headlineList = []
    for i in headlineListN:
        headlineList.append(i.strip('\n'))
        #print(i.strip('\n'))
    print(headlineList)


# # Featured Image

# PL Mars Space Images - Featured Image
# 
# Visit the url for JPL Featured Space Image here.
# https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars
# 
# 
# Use splinter to navigate the site and find the image url for the current Featured Mars Image and assign the url string to a variable called featured_image_url.
# 
# 
# Make sure to find the image url to the full size .jpg image.
# 
# 
# Make sure to save a complete url string for this image.
# #Example:
# featured_image_url = 'https://www.jpl.nasa.gov/spaceimages/images/largesize/PIA16225_hires.jpg'

# In[14]:


url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
response = requests.get(url)
soup = bs(response.text, 'html.parser')
print(soup.prettify())


# In[15]:


imagePartial = "https://www.jpl.nasa.gov"
imageUrl = imagePartial + "/spaceimages/?search=&category=Mars"
browser.visit(imageUrl)
browser.click_link_by_partial_text('FULL IMAGE')
expand = browser.find_by_css('a.fancybox-expand')

imageSearch = browser.html
imageSoup = bs(imageSearch, 'html.parser')
results = imageSoup.find('img', {"class":"fancybox-image"})['src']


# In[16]:


fullImageLink = imagePartial + results
print(fullImageLink)
print(f'{imagePartial}{results}')


# In[17]:


len(results)


# In[ ]:





# # Mars Facts
# 
# 
# Visit the Mars Facts webpage here and use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.
# https://space-facts.com/mars/
# 
# 
# Use Pandas to convert the data to a HTML table string.

# In[18]:


marsDataUrl = "https://space-facts.com/mars/"


# In[19]:


response = requests.get(marsDataUrl)
soupResponse = bs(response.text, 'html.parser')
#print(soupResponse.prettify())


# In[20]:


browser.visit(marsDataUrl)
marsDataSearch = browser.html
marsDataSoup = bs(marsDataSearch, 'html.parser')


# In[21]:


#Printing response as string to analyze
strMars = str(marsDataSoup.find_all())
print(type(strMars))
htmlStringLength = len(strMars)
print(type(htmlStringLength))
print(htmlStringLength)
partialHTML = int(htmlStringLength * .10/100)
print(strMars[:partialHTML])


# In[22]:


#Writing response to HTML file to view
htmlFile = open("response.html", "w")
htmlFile .write(strMars)
htmlFile.close()


# In[23]:


browser.visit(marsDataUrl)
marsDataSearch = browser.html
marsDataSoup = bs(marsDataSearch, 'html.parser')
results = marsDataSoup.find('table', {"class":"tablepress"})
marsList = pd.read_html(marsDataUrl)
print(type(marsList))
#print(marsList)


# In[24]:


# len(marsList)
# marsList[1]


# In[25]:


marsList[1]
marsDict = dict(marsList[1])
#marsDict[1]
marsComparisonDF = pd.DataFrame.from_dict(marsDict)
#print(type(marsComparisonDF))
marsComparisonDF


# In[26]:


marsDict = dict(marsList[0])
#marsDict[1]
marsDF = pd.DataFrame.from_dict(marsDict)
print(type(marsDF))
marsDF = marsDF.rename(columns = {0: "Measurement", 1:"Value"})
marsDF


# In[ ]:





# # Mars Hemispheres
# 
# 
# Visit the USGS Astrogeology site here to obtain high resolution images for each of Mar's hemispheres.
# https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars
# 
# 
# You will need to click each of the links to the hemispheres in order to find the image url to the full resolution image.
# 
# 
# Save both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name. Use a Python dictionary to store the data using the keys img_url and title.
# 
# 
# Append the dictionary with the image url string and the hemisphere title to a list. This list will contain one dictionary for each hemisphere.
# 
# #Example:
# hemisphere_image_urls = [
#     {"title": "Valles Marineris Hemisphere", "img_url": "..."},
#     {"title": "Cerberus Hemisphere", "img_url": "..."},
#     {"title": "Schiaparelli Hemisphere", "img_url": "..."},
#     {"title": "Syrtis Major Hemisphere", "img_url": "..."},
# ]

# In[27]:


# hemiURL = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
# browser.visit(hemiURL)
# hemiSearch = browser.html
# hemiSoup = bs(hemiSearch, 'html.parser')


# In[28]:


# browser.click_link_by_partial_text('FULL IMAGE')
# expand = browser.find_by_css('a.fancybox-expand')

# imageSearch = browser.html
# imageSoup = bs(imageSearch, 'html.parser')
# results = imageSoup.find('img', {"class":"fancybox-image"})['src']


# In[29]:


hemisphereDicts = {"Reason":"Website down unable to scrape"}


# # FLASK APPLICATION/ MONGO DB
# 
# Use MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.

# In[30]:


print(fullImageLink)


# In[31]:


marsComparisonDF


# In[32]:


marsCompareDict = marsComparisonDF.to_dict()
marsCompareDict


# In[33]:


marsDF


# In[34]:


marsDict = marsDF.to_dict()
marsDict


# In[35]:


exportDict = {
    "headlines": headlineList, 
    "imageLink": fullImageLink, 
    "DF1": marsDict, 
    "DF2": marsCompareDict, 
    "hemi": hemisphereDicts}


# In[36]:


exportDict


# In[37]:


#installing jupyter notebook converter
get_ipython().system('pip install nbconvert')


# In[38]:


#conda install nbconvert


# In[39]:


#converting ipynb to py
get_ipython().system('jupyter nbconvert --to python webScraping.ipynb')


# In[40]:


#renaming ipynb to scrape_mars.py
get_ipython().system('mv webScraping.py scrape_mars.py')


# In[ ]:


get_ipython().run_line_magic('load', 'scrape_mars.py')
#!/usr/bin/env python

# # Mission to Mars
# - this program analyzes data from the NASA website

# # Dependencies

# In[5]:


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

# In[6]:


# fileName = input("Please enter the name of the file you'd like to use.")
# while not os.path.isfile(fileName):
#     fileName = input("Whoops! No such file! Please enter the name of the file you'd like to use.")


# In[7]:


get_ipython().system('which chromedriver')


# In[8]:


# # Open default browser to web page with Mac
# !python -m webbrowser -t "https://mars.nasa.gov/news/"


# In[9]:


#driver = webdriver.Chrome(executable_path='usr/local/bin/chromedriver')


# In[10]:


# Mac
# Choose the executable path to driver 
executable_path = {'executable_path': 'chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)


# In[11]:


print(executable_path)


# # NASA Mars News
# Scrape the NASA Mars News Site and collect the latest News Title and Paragraph Text. Assign the text to variables that you can reference later.
# 
# #Example:
# news_title = "NASA's Next Mars Mission to Investigate Interior of Red Planet"
# 
# news_p = "Preparation of NASA's next spacecraft to Mars, InSight, has ramped up this summer, on course for launch next May from Vandenberg Air Force Base in central California -- the first interplanetary launch in history from America's West Coast."

# In[12]:


# # PC
# # Choose the executable path to driver
#executable_path = {'executable_path': 'chromedriver.exe'}
#browser = Browser('chrome', **executable_path, headless=Fale)


# In[13]:


url = "https://mars.nasa.gov/news/"
browser.visit(url)


# In[14]:


html = browser.html
soup = bs(html, 'html.parser')


# # Featured Image

# PL Mars Space Images - Featured Image
# 
# Visit the url for JPL Featured Space Image here.
# https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars
# 
# 
# Use splinter to navigate the site and find the image url for the current Featured Mars Image and assign the url string to a variable called featured_image_url.
# 
# 
# Make sure to find the image url to the full size .jpg image.
# 
# 
# Make sure to save a complete url string for this image.
# #Example:
# featured_image_url = 'https://www.jpl.nasa.gov/spaceimages/images/largesize/PIA16225_hires.jpg'

# In[15]:


url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
response = requests.get(url)
soup = bs(response.text, 'html.parser')
print(soup.prettify())


# In[16]:


imagePartial = "https://www.jpl.nasa.gov"
imageUrl = imagePartial + "/spaceimages/?search=&category=Mars"
browser.visit(imageUrl)
browser.click_link_by_partial_text('FULL IMAGE')
expand = browser.find_by_css('a.fancybox-expand')

imageSearch = browser.html
imageSoup = bs(imageSearch, 'html.parser')
results = imageSoup.find('img', {"class":"fancybox-image"})['src']


# In[17]:


fullImageLink = imagePartial + results
print(fullImageLink)
print(f'{imagePartial}{results}')


# In[18]:


len(results)


# In[ ]:





# # Mars Facts
# 
# 
# Visit the Mars Facts webpage here and use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.
# https://space-facts.com/mars/
# 
# 
# Use Pandas to convert the data to a HTML table string.

# In[19]:


marsDataUrl = "https://space-facts.com/mars/"


# In[20]:


response = requests.get(marsDataUrl)
soupResponse = bs(response.text, 'html.parser')
#print(soupResponse.prettify())


# In[21]:


browser.visit(marsDataUrl)
marsDataSearch = browser.html
marsDataSoup = bs(marsDataSearch, 'html.parser')


# In[22]:


#Printing response as string to analyze
strMars = str(marsDataSoup.find_all())
print(type(strMars))
htmlStringLength = len(strMars)
print(type(htmlStringLength))
print(htmlStringLength)
partialHTML = int(htmlStringLength * .10/100)
print(strMars[:partialHTML])


# In[23]:


#Writing response to HTML file to view
htmlFile = open("response.html", "w")
htmlFile .write(strMars)
htmlFile.close()


# In[24]:


browser.visit(marsDataUrl)
marsDataSearch = browser.html
marsDataSoup = bs(marsDataSearch, 'html.parser')
results = marsDataSoup.find('table', {"class":"tablepress"})
marsList = pd.read_html(marsDataUrl)
print(type(marsList))
#print(marsList)


# In[25]:


# len(marsList)
# marsList[1]


# In[26]:


marsList[1]
marsDict = dict(marsList[1])
#marsDict[1]
marsComparisonDF = pd.DataFrame.from_dict(marsDict)
#print(type(marsComparisonDF))
marsComparisonDF


# In[27]:


marsDict = dict(marsList[0])
#marsDict[1]
marsDF = pd.DataFrame.from_dict(marsDict)
print(type(marsDF))
marsDF = marsDF.rename(columns = {0: "Measurement", 1:"Value"})
marsDF


# In[ ]:





# # Mars Hemispheres
# 
# 
# Visit the USGS Astrogeology site here to obtain high resolution images for each of Mar's hemispheres.
# https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars
# 
# 
# You will need to click each of the links to the hemispheres in order to find the image url to the full resolution image.
# 
# 
# Save both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name. Use a Python dictionary to store the data using the keys img_url and title.
# 
# 
# Append the dictionary with the image url string and the hemisphere title to a list. This list will contain one dictionary for each hemisphere.
# 
# #Example:
# hemisphere_image_urls = [
#     {"title": "Valles Marineris Hemisphere", "img_url": "..."},
#     {"title": "Cerberus Hemisphere", "img_url": "..."},
#     {"title": "Schiaparelli Hemisphere", "img_url": "..."},
#     {"title": "Syrtis Major Hemisphere", "img_url": "..."},
# ]

# In[28]:


# hemiURL = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
# browser.visit(hemiURL)
# hemiSearch = browser.html
# hemiSoup = bs(hemiSearch, 'html.parser')


# In[29]:


# browser.click_link_by_partial_text('FULL IMAGE')
# expand = browser.find_by_css('a.fancybox-expand')

# imageSearch = browser.html
# imageSoup = bs(imageSearch, 'html.parser')
# results = imageSoup.find('img', {"class":"fancybox-image"})['src']


# # FLASK APPLICATION/ MONGO DB
# 
# Use MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.

# In[39]:


print(fullImageLink)


# In[50]:


marsComparisonDF


# In[49]:


marsCompareDict = marsComparisonDF.to_dict()
marsCompareDict


# In[43]:


marsDF


# In[51]:


marsDict = marsDF.to_dict()
marsDict


# In[54]:


exportDict = {"imageLink": fullImageLink, "DF1": marsDict, "DF2": marsCompareDict}


# In[55]:


exportDict


# In[ ]:





# In[ ]:


#installing jupyter notebook converter
get_ipython().system('pip install nbconvert')


# In[ ]:


#conda install nbconvert


# In[ ]:


#converting ipynb to py
get_ipython().system('jupyter nbconvert --to python webScraping.ipynb')


# In[34]:


#renaming ipynb to scrape_mars.py
get_ipython().system('mv webScraping.py scrape_mars.py')


# In[ ]:


# %load scrape_mars.py
#!/usr/bin/env python

# # Mission to Mars
# - this program analyzes data from the NASA website

# # Data Analysis Functions
# - Currently set as functions/Module call not working
# - Run Modules 
# - getTypes, 
# - describeData, 
# - analyzeNaNs
# #Before import

# In[1]:


#%%writefile getTypes.py
# Comment: Write file creates a module that can be imported with dependencies, %%writefile -a getTypes.py, remove if func is changed

import pandas as pd
import numpy as np
import requests
import os
import json
import matplotlib.pyplot as plt
from IPython.core.display import HTML
from datetime import date, datetime



# In[2]:


#%%writefile describeData.py
# Comment: Write file creates a module that can be imported with dependencies, %%writefile -a describeData.py appends, remove if func is changed
# Comment: This function prints stats for strings and integer value columns
import pandas as pd
import numpy as np
import requests
import os
import json
import matplotlib.pyplot as plt
from IPython.core.display import HTML
from datetime import date, datetime

def describeData(dataFrameName):
    print('Executing describeData...')
    print('-------------------------------')
    global keyHeaders, colsData, stringDescribe, intDescribe, keyStr, KeyInt
    keyStr, keyInt, keyHeaders, intDescribe, stringDescribe = [], [], [], [], []
    for key, value in dataFrameName.items():
        #grabs cols as keys into list
        keyHeaders.append(key)
    for i in keyHeaders:
        #checks the cols data if string
        if isinstance(dataFrameName[i][0], (str)):
            stringDescribe.append(dataFrameName[keyHeaders][i].describe())
        else:
            intDescribe.append(dataFrameName[keyHeaders][i].describe())
    stringDescribe = pd.DataFrame.from_dict(dict(zip(keyHeaders, stringDescribe)), orient='index')
    intDescribe = pd.DataFrame.from_dict(dict(zip(keyHeaders, intDescribe)), orient='index') 
    #adding pretty print to dataframes, don't forget import statment when copying code
    print('-------------------------------')
    print('Object Describe Dataframe')
    print('-------------------------------')
    display(HTML(stringDescribe.to_html()))
    #print(stringDescribe)
    print('-------------------------------')
    print('Integer/FloatDescribe Dataframe')
    print('-------------------------------')
    display(HTML(intDescribe.to_html()))
    #print(intDescribe)
    lengthofDF = len(dataFrameName)
    print('-------------------------------')
    print(f'Dataframe Length: {lengthofDF}')
    print('-------------------------------')
    columnNames = dataFrameName.columns.tolist()
    print(f'ColumnNames: \n{columnNames}')
# Comment: by ph1-6180


# In[3]:


#%%writefile analyzeNaNs.py
# Comment: Write file creates a module that can be imported with dependencies, %%writefile -a analyzeNaNs.py appends, remove if func is changed
# Comment: This function analyzes the NaN's in a DF
# Comment: Print/Returns a Dataframe with the NaN's count and the list of columns without NaN's
import pandas as pd
import numpy as np
import requests
import os
import json
import matplotlib.pyplot as plt
from IPython.core.display import HTML
from datetime import date, datetime

def analyzeNaNs(dataFrameName):
    print('Executing analyzeNaNs...')
    print('---------------------')
    columnNames = dataFrameName.columns.tolist()
    NaNslist = []
    noNaNs =[]
    counter = 0
    for i in columnNames:
        colNaNs = dataFrameName[i].isna().sum()
        NaNslist.append(colNaNs)
        #print(f'{colNaNs} NaNs in {columnNames[counter]}')
        counter += 1
    #print(NaNslist)
    #print(columnNames)
    NaNsDF = pd.DataFrame(NaNslist, index = columnNames, columns =['NaNsCount'])
    transposeDF = NaNsDF.T
    for i in columnNames:
        if transposeDF[i][0] == 0:
            noNaNs.append(i)
            transposeDF = transposeDF.drop([i], axis=1)
    print('----------------------')
    print('Columns NoNaNs::')
    print('----------------------')
    for j in range(len(noNaNs)):
        alphaCols = sorted(noNaNs)
        print(f'{alphaCols[j]}')
    print('\n\n\n---------------------')
    print('NaNs Count DataFrame::')
    print('---------------------')
    display(HTML(transposeDF.to_html()))
    #print(transposeDF)
# Comment: by ph1-6180


# # Install Modules
# - Currently commented out because errors with calling *.py files to run

# In[4]:


# !python Modules/getTypes.py
# !python Modules/describeData.py
# !python Modules/analyzeNaNs.py


# In[5]:


# Dependencies
#import getTypes
#import describeData
#import analyzeNaNs
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

# In[6]:


# fileName = input("Please enter the name of the file you'd like to use.")
# while not os.path.isfile(fileName):
#     fileName = input("Whoops! No such file! Please enter the name of the file you'd like to use.")


# In[7]:


get_ipython().system('which chromedriver')


# In[8]:


# # Open default browser to web page with Mac
# !python -m webbrowser -t "https://mars.nasa.gov/news/"


# In[9]:


#driver = webdriver.Chrome(executable_path='usr/local/bin/chromedriver')


# In[10]:


# Mac
# Choose the executable path to driver 
executable_path = {'executable_path': 'chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)


# In[11]:


print(executable_path)


# # NASA Mars News
# Scrape the NASA Mars News Site and collect the latest News Title and Paragraph Text. Assign the text to variables that you can reference later.
# 
# #Example:
# news_title = "NASA's Next Mars Mission to Investigate Interior of Red Planet"
# 
# news_p = "Preparation of NASA's next spacecraft to Mars, InSight, has ramped up this summer, on course for launch next May from Vandenberg Air Force Base in central California -- the first interplanetary launch in history from America's West Coast."

# In[12]:


# # PC
# # Choose the executable path to driver
#executable_path = {'executable_path': 'chromedriver.exe'}
#browser = Browser('chrome', **executable_path, headless=Fale)


# In[13]:


url = "https://mars.nasa.gov/news/"
browser.visit(url)


# In[14]:


html = browser.html
soup = bs(html, 'html.parser')


# # Featured Image

# PL Mars Space Images - Featured Image
# 
# Visit the url for JPL Featured Space Image here.
# https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars
# 
# 
# Use splinter to navigate the site and find the image url for the current Featured Mars Image and assign the url string to a variable called featured_image_url.
# 
# 
# Make sure to find the image url to the full size .jpg image.
# 
# 
# Make sure to save a complete url string for this image.
# #Example:
# featured_image_url = 'https://www.jpl.nasa.gov/spaceimages/images/largesize/PIA16225_hires.jpg'

# In[15]:


url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
response = requests.get(url)
soup = bs(response.text, 'html.parser')
print(soup.prettify())


# In[16]:


imagePartial = "https://www.jpl.nasa.gov"
imageUrl = imagePartial + "/spaceimages/?search=&category=Mars"
browser.visit(imageUrl)
browser.click_link_by_partial_text('FULL IMAGE')
expand = browser.find_by_css('a.fancybox-expand')

imageSearch = browser.html
imageSoup = bs(imageSearch, 'html.parser')
results = imageSoup.find('img', {"class":"fancybox-image"})['src']


# In[17]:


fullImageLink = imagePartial + results
print(fullImageLink)
print(f'{imagePartial}{results}')


# In[18]:


len(results)


# In[ ]:





# # Mars Facts
# 
# 
# Visit the Mars Facts webpage here and use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.
# https://space-facts.com/mars/
# 
# 
# Use Pandas to convert the data to a HTML table string.

# In[19]:


marsDataUrl = "https://space-facts.com/mars/"


# In[20]:


response = requests.get(marsDataUrl)
soupResponse = bs(response.text, 'html.parser')
#print(soupResponse.prettify())


# In[21]:


browser.visit(marsDataUrl)
marsDataSearch = browser.html
marsDataSoup = bs(marsDataSearch, 'html.parser')


# In[22]:


#Printing response as string to analyze
strMars = str(marsDataSoup.find_all())
print(type(strMars))
htmlStringLength = len(strMars)
print(type(htmlStringLength))
print(htmlStringLength)
partialHTML = int(htmlStringLength * .10/100)
print(strMars[:partialHTML])


# In[23]:


#Writing response to HTML file to view
htmlFile = open("response.html", "w")
htmlFile .write(strMars)
htmlFile.close()


# In[24]:


browser.visit(marsDataUrl)
marsDataSearch = browser.html
marsDataSoup = bs(marsDataSearch, 'html.parser')
results = marsDataSoup.find('table', {"class":"tablepress"})
marsList = pd.read_html(marsDataUrl)
print(type(marsList))
#print(marsList)


# In[25]:


# len(marsList)
# marsList[1]


# In[26]:


marsList[1]
marsDict = dict(marsList[1])
#marsDict[1]
marsComparisonDF = pd.DataFrame.from_dict(marsDict)
#print(type(marsComparisonDF))
marsComparisonDF


# In[27]:


marsDict = dict(marsList[0])
#marsDict[1]
marsDF = pd.DataFrame.from_dict(marsDict)
print(type(marsDF))
marsDF = marsDF.rename(columns = {0: "Measurement", 1:"Value"})
marsDF


# In[ ]:





# # Mars Hemispheres
# 
# 
# Visit the USGS Astrogeology site here to obtain high resolution images for each of Mar's hemispheres.
# https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars
# 
# 
# You will need to click each of the links to the hemispheres in order to find the image url to the full resolution image.
# 
# 
# Save both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name. Use a Python dictionary to store the data using the keys img_url and title.
# 
# 
# Append the dictionary with the image url string and the hemisphere title to a list. This list will contain one dictionary for each hemisphere.
# 
# #Example:
# hemisphere_image_urls = [
#     {"title": "Valles Marineris Hemisphere", "img_url": "..."},
#     {"title": "Cerberus Hemisphere", "img_url": "..."},
#     {"title": "Schiaparelli Hemisphere", "img_url": "..."},
#     {"title": "Syrtis Major Hemisphere", "img_url": "..."},
# ]

# In[28]:


# hemiURL = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
# browser.visit(hemiURL)
# hemiSearch = browser.html
# hemiSoup = bs(hemiSearch, 'html.parser')


# In[29]:


# browser.click_link_by_partial_text('FULL IMAGE')
# expand = browser.find_by_css('a.fancybox-expand')

# imageSearch = browser.html
# imageSoup = bs(imageSearch, 'html.parser')
# results = imageSoup.find('img', {"class":"fancybox-image"})['src']


# # FLASK APPLICATION/ MONGO DB
# 
# Use MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.

# In[30]:


print(marsComparisonDF)
print(marsDF)


# In[32]:


get_ipython().system('jupyter nbconvert --to python webScraping.ipynb')


# In[ ]:


get_ipython().system('mv webScraping.py ')


# In[ ]:


# %%writefile scrape_mars.py


# Start by converting your Jupyter notebook into a Python script called scrape_mars.py with a function called scrape that will execute all of your scraping code from above and return one Python dictionary containing all of the scraped data.

# In[ ]:





# Next, create a route called /scrape that will import your scrape_mars.py script and call your scrape function.

# In[ ]:





# Store the return value in Mongo as a Python dictionary.

# In[ ]:





# Create a root route / that will query your Mongo database and pass the mars data into an HTML template to display the data.

# In[ ]:





# Create a template HTML file called index.html that will take the mars data dictionary and display all of the data in the appropriate HTML elements. Use the following as a guide for what the final product should look like, but feel free to create your own design.

# In[ ]:





# In[ ]:


# %%writefile scrape_mars.py


# Start by converting your Jupyter notebook into a Python script called scrape_mars.py with a function called scrape that will execute all of your scraping code from above and return one Python dictionary containing all of the scraped data.

# In[ ]:





# Next, create a route called /scrape that will import your scrape_mars.py script and call your scrape function.

# In[ ]:





# Store the return value in Mongo as a Python dictionary.

# In[ ]:





# Create a root route / that will query your Mongo database and pass the mars data into an HTML template to display the data.

# In[ ]:





# Create a template HTML file called index.html that will take the mars data dictionary and display all of the data in the appropriate HTML elements. Use the following as a guide for what the final product should look like, but feel free to create your own design.

# In[ ]:





# In[42]:


# %%writefile scrape_mars.py


# Start by converting your Jupyter notebook into a Python script called scrape_mars.py with a function called scrape that will execute all of your scraping code from above and return one Python dictionary containing all of the scraped data.

# In[ ]:





# Next, create a route called /scrape that will import your scrape_mars.py script and call your scrape function.

# In[ ]:





# Store the return value in Mongo as a Python dictionary.

# In[ ]:





# Create a root route / that will query your Mongo database and pass the mars data into an HTML template to display the data.

# In[ ]:





# Create a template HTML file called index.html that will take the mars data dictionary and display all of the data in the appropriate HTML elements. Use the following as a guide for what the final product should look like, but feel free to create your own design.

# In[ ]:




