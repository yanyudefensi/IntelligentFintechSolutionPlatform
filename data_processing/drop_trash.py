#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import jieba
import numpy as np
import os


# In[2]:


df_tech = pd.read_csv(r'D:\机器学习\爬虫数据\fintech\物联网-人工智能实验室-2019.4..csv',engine='python')   #文章路径名字


# In[3]:


df_tech


# ## content去掉？？后的内容

# In[4]:


def content_clean(content):
    try:
        if '??次阅读来源：' in content:
            content_list = content.split('\t')
            content_list.remove(content_list[0])
            content_clean = '\t'.join(content_list)
        return content_clean
    except:
        return content


# ## title去掉来源之后的内容

# In[5]:


def title_clean(title):
    try:
        location = title.find('来源')
        title = title[:location]
        return title
    except:
        return title


# In[6]:


df_tech['content'] = df_tech['content'].apply(content_clean)


# In[7]:


df_tech['title'] = df_tech['title'].apply(title_clean)


# ## summary列取content的前40个字符

# In[8]:


for i in range(len(df_tech)):
    
    df_tech.loc[i,'summary'] = str(df_tech.loc[i,'content'])[:40]


# In[9]:


df_tech.to_csv(r'D:\机器学习\爬虫数据\fintech\物联网-人工智能实验室-2019.4..csv',index=False,encoding='utf_8_sig')


# In[ ]:




