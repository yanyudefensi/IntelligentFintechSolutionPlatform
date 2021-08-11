#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import jieba
import numpy as np
import os


# ## 数据清洗，去换行符等

# In[2]:


#删除换行符，以及单双引号
def clean(var):
    if isinstance(var,str):
        var=var.strip().replace('\n','').replace(' ','').replace('\"','').replace('\'','').replace('‘','').replace('’','').replace('“','').replace('”','')
        
        if var.endswith('\\'):
            var = var[:-1]      #以符号结尾的也不行
                    
    return var


# In[3]:


'''重命名'''
def rename_duplicate(list_title,list_vendor, print_result=False):
    new_list=[str(v) +'_'+ str(list_vendor[i]) if list_title.count(v) > 1 else v for i, v in enumerate(list_title)]
    if print_result:
        print("Renamed list:",new_list)
    return new_list


# In[4]:


#对解决方案清洗
def vendor_clean(data):
    if 'vendor' in data.columns:
        data.drop(columns=['vendor'],inplace=True)
    cols=[col for col in data.columns if col not in ['type','url']]
    for col in cols:
        data[col]=data[col].apply(clean)

    data=data.drop_duplicates(['title'])
    return data


# In[5]:


vendor = pd.read_csv(r'D:\机器学习\爬虫数据\vendors\服务供应商.csv',engine='python')

vendor = vendor_clean(vendor)

vendor.reset_index(drop=True,inplace=True)
vendor=vendor[['type', 'url', 'title', 'content', 'summary']]

vendor.to_csv(r'D:\机器学习\实体关系数据\vendor.csv',index=False,encoding='utf_8_sig')

