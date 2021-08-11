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


'''对不同企业痛同方案重命名'''
def rename_duplicate(list_title,list_vendor, print_result=False):
    new_list=[str(v) +'_'+ str(list_vendor[i]) if list_title.count(v) > 1 else v for i, v in enumerate(list_title)]
    if print_result:
        print("Renamed list:",new_list)
    return new_list


# In[4]:


'''对同企业同解决方案重命名'''
def rename_duplicate2(list, print_result=False):
    new_list=[v + str(list[:i].count(v) + 1) if list.count(v) > 1 else v for i, v in enumerate(list)]
    if print_result:
        print("Renamed list:",new_list)
    return new_list


# In[5]:


#对解决方案清洗
def solutions_clean(data):
    cols=[col for col in data.columns if col not in ['type','url','vendor']]
    for col in cols:
        data[col]=data[col].apply(clean)
        
    try:
        data=data[data['type'] == '1']     #如果是其他类型2要改！！！！
    except:
        print('')
#     data=data.fillna('1')
#     data=data[data['content'] != '1']
#     data=data[data['summary'] != '1']      #进一步进行处理，去掉content 和summary 没有的行

    data=data.drop_duplicates(['title'])
    return data


# '''测试'''
# # df = pd.read_csv(r'C:\Users\10175\Desktop\机器学习\爬虫数据\fintech\云计算-百度百科-2019.4..csv',engine='python')
# df = tech_clean(df)
# df.reset_index(drop=True,inplace=True)
# df=df[['type', 'url', 'title', 'content', 'summary','vendor']]
# 
# df
# # df.to_csv(r'C:\Users\10175\Desktop\机器学习\实体关系数据\技术文章实体\df.csv',index=False,encoding='utf_8_sig')

# In[6]:


path = r"D:\机器学习\爬虫数据\solutions"    #原始文件存放地方

files = os.listdir(path)

ls = []
for file in files:
    domain = os.path.abspath(path)
    file_path = os.path.join(domain, file)

    try:
        df_solution = pd.read_csv(file_path,engine='python')
        df_solution=solutions_clean(df_solution)
        df_solution.reset_index(drop=True,inplace=True)

        df_solution=df_solution[['type', 'url', 'title', 'content', 'summary','vendor']]
#         df_solution.to_csv(r'D:\机器学习\实体关系数据\技术文章实体\%s'%file,index=False,encoding='utf_8_sig')

        ls.append(df_solution)
    except:
        e

solution=pd.concat(ls) #合并所有解决方案


# In[7]:


solution['title']=rename_duplicate([i for i in solution.title],[j for j in solution.vendor])


# In[8]:


solution['title']=rename_duplicate2([i for i in solution.title])


# In[9]:


solution = solution.drop_duplicates(['title'])
solution.reset_index(drop=True,inplace=True)


# In[11]:


solution.to_csv(r'D:\机器学习\实体关系数据\solution.csv',index=False,encoding='utf_8_sig')


# In[ ]:




