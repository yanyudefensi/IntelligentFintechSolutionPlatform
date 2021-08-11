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


'''对list项里重复的值重命名'''
def rename_duplicate(list, print_result=False):
    new_list=[v + str(list[:i].count(v) + 1) if list.count(v) > 1 else v for i, v in enumerate(list)]
    if print_result:
        print("Renamed list:",new_list)
    return new_list


# In[4]:


#对技术文章的清洗
#删除vendor字段，对其他字段调用clean函数
def tech_clean(data):
    if 'vender' in data.columns:
        data.drop(columns=['vender'],inplace=True)
    cols=[col for col in data.columns if col not in ['type','url']]
    for col in cols:
        data[col]=data[col].apply(clean)
        
    try:
        data=data[data['type'] == '2']     #如果是其他类型2要改！！！！
    except:
        print('')
#     data=data.fillna('1')
#     data=data[data['content'] != '1']
#     data=data[data['summary'] != '1']      #进一步进行处理，去掉content 和summary 没有的行

    data=data.drop_duplicates(['title'])
    return data


# '''测试'''
# df = pd.read_csv(r'C:\Users\10175\Desktop\机器学习\爬虫数据\fintech\云计算-百度百科-2019.4..csv',engine='python')
# df = tech_clean(df)
# df.reset_index(drop=True,inplace=True)
# df=df[['type', 'url', 'title', 'content', 'summary']]
# df.to_csv(r'C:\Users\10175\Desktop\机器学习\实体关系数据\技术文章实体\df.csv',index=False,encoding='utf_8_sig')

# In[7]:


#解决字段超出限制
import sys
import csv
# csv.field_size_limit(100000 * 1024 * 1024) 7
# csv.field_size_limit(sys.maxsize)


# In[8]:


path = r"D:\机器学习\爬虫数据\fintech"    #原始文件存放地方

files = os.listdir(path)

ls = []
for file in files:
    domain = os.path.abspath(path)
    file_path = os.path.join(domain, file)

#     print(file)
    try:
        df_tech = pd.read_csv(file_path,engine='python')
        df_tech=tech_clean(df_tech)
        df_tech.reset_index(drop=True,inplace=True)

        col=df_tech.columns
        df_tech=df_tech[['type', 'url', 'title', 'content', 'summary']]
#         df_tech.to_csv(r'D:\机器学习\实体关系数据\技术文章实体\%s'%file,index=False,encoding='utf_8_sig')

        ls.append(df_tech)

        solution=pd.concat(ls) #合并所有解决方案


    except:
        print(file_path)


# In[14]:


solution = solution.drop_duplicates(['title'])
solution.reset_index(drop=True,inplace=True)


# In[22]:


solution[0:50000].to_csv(r'D:\机器学习\实体关系数据\tech_entity1.csv',index=False,encoding='utf_8_sig')


# In[23]:


solution[50000:100000].to_csv(r'D:\机器学习\实体关系数据\tech_entity2.csv',index=False,encoding='utf_8_sig')


# In[24]:


solution[100000:150000].to_csv(r'D:\机器学习\实体关系数据\tech_entity3.csv',index=False,encoding='utf_8_sig')


# In[25]:


solution[150000:200000].to_csv(r'D:\机器学习\实体关系数据\tech_entity4.csv',index=False,encoding='utf_8_sig')


# In[26]:


solution[200000:].to_csv(r'D:\机器学习\实体关系数据\tech_entity5.csv',index=False,encoding='utf_8_sig')


# In[ ]:




