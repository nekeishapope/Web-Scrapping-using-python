#!/usr/bin/env python
# coding: utf-8

# In[112]:


import requests 
from requests_html import HTMLSession
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd


# In[121]:


#get the web url that you want to scrape
url = 'https://medium.com/@nekeishapope/the-power-of-data-analysis-146551c3bbab'

#send a request to the website
response = requests.get(url)

#use soup to parse a particluar content from the page
soup = BeautifulSoup(response.content, 'html.parser')

#for loop to go through the text on the webpage
for element in soup(['script', 'style', 'comment']):
    text = soup.get_text(separator=' ')
print(text)


# In[ ]:




