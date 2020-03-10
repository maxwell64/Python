#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import datetime

url = 'https://uk.finance.yahoo.com/quote/GOOG?p=GOOG&.tsrc=fin-srch'
indicators  = ['Previous close', 'Open', 'Bid', 'Ask', 'Market cap']
f = open('/home/maxwell/Documents/pythonStuff/web_scraper/GOOG.txt', 'a')


# In[2]:


#import the response from the page
response = requests.get(url)


# In[3]:


#define the html text from the page
html_text = response.text


# In[4]:


#prints the date and time for reference/comparison
print(datetime.datetime.today())
s = '\n{}\n'.format(datetime.datetime.today())
f.write(s)

#cycles through the indicators and acquires the data for each
for i in indicators:
    split_text = html_text.split(i)
    split2 = split_text[1].split('">')
    split3 = split2[2].split('</span>')
    data = split3[0]
    s = '{} : ${}\n'.format(i, data)
    print(s)
    f.write(s)
    
f.close()


# In[ ]:




