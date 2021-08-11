from elasticsearch import Elasticsearch
import os
import csv


# 设置csv文件字段的最大长度
csv.field_size_limit(500 * 1024 * 1024)
# 文件目录
VENDOR_DIR = '/home/scut2/data/vendors/'
ARTICLE_DIR = '/home/scut2/data/articles/'
SOLUTION_DIR = '/home/scut2/data/solutions/'
FINTECH_DIR = '/home/scut2/data/fintech/'
# VENDOR_DIR = 'F:/vendors/'
# ARTICLE_DIR = 'F:/articles/'
# SOLUTION_DIR = 'F:/solutions/'

class Inputor():
    def __init__(self):
        self.es = Elasticsearch(hosts=[{'host': 'localhost', 'port': 9000}])

    # 导入供应商数据
    def input_vendors(self):
        for path in os.listdir(VENDOR_DIR):
            filename = VENDOR_DIR + path
            print(filename)
            with open(filename, 'r', encoding='utf-8-sig') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    doc = {
                        'type': int(row['type']),
                        'url': row['url'],
                        'title': row['title'],
                        'summary': row['summary'],
                        'content': row['content']
                    }
                    res = self.es.index(index='vendor', doc_type='_doc', body=doc)
                    print(res)

    # 导入解决方案数据
    def input_solutions(self):
        for path in os.listdir(SOLUTION_DIR):
            filename = SOLUTION_DIR + path
            print(filename)
            try:
                with open(filename, 'r', encoding='utf-8-sig') as f:
                    reader = csv.DictReader(f)
                    for row in reader:
                        doc = {
                            'type': int(row['type']),
                            'url': row['url'],
                            'title': row['title'],
                            'summary': row['summary'],
                            'content': row['content'],
                            'vendor': row['vendor']
                        }
                        res = self.es.index(index='solution', doc_type='_doc', body=doc)
            except:
                with open(filename, 'r', encoding='gbk') as f:
                    reader = csv.DictReader(f)
                    for row in reader:
                        doc = {
                            'type': int(row['type']),
                            'url': row['url'],
                            'title': row['title'],
                            'summary': row['summary'],
                            'content': row['content'],
                            'vendor': row['vendor']
                        }
                        res = self.es.index(index='solution', doc_type='_doc', body=doc)
                        print(res)

    # 导入技术文章数据
    def input_articles(self):
        for path in os.listdir(ARTICLE_DIR):
            filename = ARTICLE_DIR + path
            print(filename)
            try:
                with open(filename, 'r', encoding='utf-8-sig') as f:
                    reader = csv.DictReader(f)
                    for row in reader:
                        try:
                            doc = {
                                'type': int(row['type']),
                                'url': row['url'],
                                'title': row['title'],
                                'summary': row['summary'],
                                'content': row['content']
                            }
                            res = self.es.index(index='article', doc_type='_doc', body=doc)
                            print(res)
                        except:
                            pass
            except:
                with open(filename, 'r', encoding='gbk') as f:
                    reader = csv.DictReader(f)
                    for row in reader:
                        try:
                            doc = {
                                'type': int(row['type']),
                                'url': row['url'],
                                'title': row['title'],
                                'summary': row['summary'],
                                'content': row['content']
                            }
                            res = self.es.index(index='article', doc_type='_doc', body=doc)
                            print(res)
                        except:
                            pass

    # 五大本体
    def input_fintech(self):
        for path in os.listdir(FINTECH_DIR):
            filename = FINTECH_DIR + path
            print(filename)
            try:
                with open(filename, 'r', encoding='utf-8-sig') as f:
                    reader = csv.DictReader(f)
                    for row in reader:
                        try:
                            doc = {
                                'title': row['title'],
                                'summary': row['summary'],
                                'content': row['content']
                            }
                            res = self.es.index(index='fintech', doc_type='_doc', body=doc)
                            print(res)
                        except:
                            pass
            except:
                with open(filename, 'r', encoding='gbk') as f:
                    reader = csv.DictReader(f)
                    for row in reader:
                        try:
                            doc = {
                                'title': row['title'],
                                'summary': row['summary'],
                                'content': row['content']
                            }
                            res = self.es.index(index='fintech', doc_type='_doc', body=doc)
                            print(res)
                        except:
                            pass

    # 启动方法
    def startup(self):
        self.input_vendors()
        self.input_solutions()
        self.input_articles()
        self.input_fintech()
        print('数据录入结束')


inputor = Inputor()
inputor.startup()
