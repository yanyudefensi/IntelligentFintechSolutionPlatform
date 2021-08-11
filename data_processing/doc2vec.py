import pandas as pd
import jieba
import gensim
from gensim.models.doc2vec import Doc2Vec, LabeledSentence
from gensim import models
from gensim import corpora,similarities
import os

# ls=[]
# path = r'D:\机器学习大project\项目数据\解决方案'
# files = os.listdir(path)
# # print(files)
# for file in files:
#     domain = os.path.abspath(path)
#     file = os.path.join(domain, file)
#     ls.append(pd.read_csv(file,engine='python',encoding='utf_8'))
# # ls[0]
# solution=pd.concat(ls) #合并所有解决方案
# solution.reset_index(drop=True,inplace=True)
# #solution

solution = pd.read_csv(r"D:\机器学习大project\项目数据\解决方案\solution_entity.csv")

stopwords = [line.strip() for line in open(r"D:\机器学习大project\nlp部分\stopwords.txt", 'r',encoding='utf-8').readlines()]

'''删除换行符，以及单双引号'''
# def clean(var):
#     if isinstance(var,str):
#         var=var.strip().replace('\n','').replace(' ','').replace('\"','').replace('\'','').replace('‘','')
#           .replace('’','').replace('“','').replace('”','')
#     return var

'''对list项里重复的值重命名'''
# def rename_duplicate(list, print_result=False):
#     new_list=[v + str(list[:i].count(v) + 1) if list.count(v) > 1 else v for i, v in enumerate(list)]
#     if print_result:
#         print("Renamed list:",new_list)
#     return new_list

#对技术文章的清洗
#删除vendor字段，对其他字段调用clean函数
# def tech_clean(data):
#     if 'vender' in data.columns:
#         data.drop(columns=['vender'],inplace=True)
#     cols=[col for col in data.columns if col not in ['type','url']]
#     for col in cols:
#         data[col]=data[col].apply(clean)
#     data=data.drop_duplicates(['title'])
#     return data

'''结巴分词并去除停用词,并去除空格换行符，同时输出解决方案实体'''
def chinese_word_cut(text):
    seg_list = []
    seg_text = jieba.cut(text)
    for word in seg_text:
        if word not in stopwords:
            if word.strip()!='':
                seg_list.append(word.strip())
    return seg_list

# solution=solutions_clean(solution)

solution['content_cut']=solution['content'].astype('str').apply(chinese_word_cut)
solution.dropna(inplace=True)
solution.reset_index(drop=True,inplace=True)

#保存解决方案实体
# solution_entity=solution.drop(columns=['content_cut'])
# solution_entity.to_csv(r'D:\机器学习大project\准备上传数据\solution_entity.csv',index=False)

'''模型训练和保存
用taggedDocument把分好的词组转化，便于丢进doc2vec训练，document1存的是全部的文章'''

document1=[]
for i in range(len(solution)):
    need=gensim.models.doc2vec.TaggedDocument(solution['content_cut'][i], tags=[str(solution['title'][i])])#用title作为标签，便于确认那个文章和目标文章最匹配
    document1.append(need)
# document1

model_dm = Doc2Vec(document1, min_count=1, window=3, vector_size=200, sample=1e-3, negative=5, workers=4)
model_dm.train(document1, total_examples=model_dm.corpus_count, epochs=70)

model_dm.save('doc2vec_model')

'''技术文章与解决方案进行匹配
读入技术文章，并进行分词,去除换行符空格等'''

'''这里批量读入了技术文章'''
ls_tech=[]
path_tech = r'D:\机器学习大project\项目数据\技术文章'
files = os.listdir(path_tech)
for file in files:
    domain = os.path.abspath(path_tech)
    file = os.path.join(domain, file)
    ls_tech.append(file)

# data=pd.read_csv(r"D:\机器学习大project\项目数据\fintech_csv\csdn_ds.csv")
# data=tech_clean(data)
# data['content_cut']=data['content'].astype('str').apply(chinese_word_cut)
# data.dropna(inplace=True)
# data.reset_index(drop=True,inplace=True)

#保存技术文章实体
# tech_entity=data.drop(columns=['content_cut'])
# tech_entity.to_csv('output/tech_entity.csv',index=False)

'''找出与技术文章匹配度最高的解决方案，取匹配度最高的五个,建立关系,并导出csv'''

# relation=pd.DataFrame(columns=['solution','relation','tech'])

# model_dm = Doc2Vec.load("doc2vec_model")
# for i in range(len(data)):
#     try:
#         inferred_vector_dm = model_dm.infer_vector(list(data['content_cut'][i]))
#         sims = model_dm.docvecs.most_similar([inferred_vector_dm], topn=5)#选出前五个最合适的匹配对象
#         print(data['title'][i],'\n',sims,'\n')
#         for j in range(0,5):
#             relation=relation.append(pd.DataFrame({'solution':[sims[j][0]],'relation':['use'],'tech':[data['title'][i]]}),ignore_index=True)
#     except TypeError:
#         print(i)
#         print('这个字段匹配不了')


'''批量输出关系函数'''


def output():
    for tech in ls_tech:
        data = pd.read_csv(tech)
        data['content_cut'] = data['content'].astype('str').apply(chinese_word_cut)
        data.dropna(inplace=True)
        data.reset_index(drop=True, inplace=True)

        relation = pd.DataFrame(columns=['solution', 'relation', 'tech'])

        model_dm = Doc2Vec.load("doc2vec_model")

        for i in range(len(data)):
            try:
                inferred_vector_dm = model_dm.infer_vector(list(data['content_cut'][i]))
                sims = model_dm.docvecs.most_similar([inferred_vector_dm], topn=5)  # 选出前五个最合适的匹配对象
                print(data['title'][i], '\n', sims, '\n')
                for j in range(0, 5):
                    relation = relation.append(
                        pd.DataFrame({'solution': [sims[j][0]], 'relation': ['use'], 'tech': [data['title'][i]]}),
                        ignore_index=True)
            except TypeError:
                print(i)
                print('这个字段匹配不了')

        relation.to_csv(r'D:\机器学习大project\项目数据\批量导出输出关系\relation_' + str(tech[26:]), index=False)
        print('完成该文件输出')


if __name__ == '__main__':
    output()

