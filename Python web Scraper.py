#!/usr/bin/env python
# coding: utf-8

# # Importing Required libraries

# In[62]:


import requests
import bs4
import articleDateExtractor
from newspaper import Article 
import pandas as pd


# # Creating generalized code for News analysis

# In[129]:


class news_analysis:
    def __init__(self,keyword):
        self.keyword = keyword
        self.url = "https://www.google.com/search?q={0}&source=lnms&tbm=nws".format(self.keyword)
        
    def run(self):           # <run> function returns the list of links associated with the keywords from google search engine            
        page = "&page="
        count = 1
        pagesToScrape = 4 
        list_links=[]
        while count <= pagesToScrape:
            scrapeURL = self.url + page + str(count)
            req = requests.get(scrapeURL)
            soup = bs4.BeautifulSoup(req.text, 'lxml')
            links = soup.find_all('a')    
            for link in links:
                l = link['href']
                if l[0:4]=='/url':
                    list_links.append(l[7:])
            count+=1
        return list_links
    
    def parse_href(self,list_links):          #<parse_href> function parses the <href> component only from the links
        href = []
        for link in links:
            if ".html" in link:
                h = link.split('&')[0]
                href.append(h)
        return href
    
    def process_articles(self,list_of_links):   #<process_articles> funtion extracts the useful content from the links related to the keywords
        Title = []
        Text = []
        Summary = []
        for link in list_of_links:
            url = link
            article = Article(url, language = 'en')
            article.download()
            article.parse()
            article.nlp()
            title = article.title
            text = article.text
            summary = article.summary
            Title.append(title)
            Text.append(text)
            Summary.append(summary)
        return Title, Text, Summary
    
    
                                 
    def get_date(self,list_of_links):    #<get_date> function extracts the publishing date of the news articles 
        dates = []
        for link in list_of_links:
            date = articleDateExtractor.extractArticlePublishedDate(link)
            dates.append(date)
        return dates


# In[99]:


news1 = news_analysis('Haryana Cabinet Approves Delhi-Gurugram-SNB RRTS Corridor')


# In[100]:


links = news1.run()


# In[101]:


valid_links = news1.parse_href(links)


# In[102]:


len(valid_links)


# In[103]:


Headline, Article, News_summary = news1.process_articles(valid_links) 


# In[ ]:


dates = news1.get_date(valid_links)


# In[112]:


news_data = pd.DataFrame({'Headlines':Headline, 'News Items': News_summary, 'News Aricle': Article, 'date-time': dates})


# In[127]:


output = news_data.to_excel('News Data.xlsx')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




