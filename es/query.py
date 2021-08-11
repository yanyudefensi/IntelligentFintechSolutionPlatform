from elasticsearch import Elasticsearch


class EsQuery():
    def __init__(self):
        self.es = Elasticsearch(hosts=[{'host': '114.116.189.184', 'port': 9000}])

    def query_vendors(self, query_str):
        res = self.es.search(
            index='vendor',
            body={
                '_source': ['url', 'title', 'summary'],
                'query': {
                    'match': {'summary': query_str}
                }
            })
        vendors = {
            'total': res['hits']['total']['value'],
            'content': []
        }
        for item in res['hits']['hits']:
            vendors['content'].append(item['_source'])

        return vendors

    def query_solutions(self, query_str):
        res = self.es.search(
            index='solution',
            body={
                '_source': ['url', 'title', 'summary'],
                'query': {
                    'match': {'summary': query_str}
                }
            })
        solutions = {
            'total': res['hits']['total']['value'],
            'content': []
        }
        for item in res['hits']['hits']:
            solutions['content'].append(item['_source'])

        return solutions

    def query_articles(self, query_str):
        res = self.es.search(
            index='article',
            body={
                '_source': ['url', 'title', 'summary'],
                'query': {
                    'match': {'summary': query_str}
                }
            })
        articles = {
            'total': res['hits']['total']['value'],
            'content': []
        }
        for item in res['hits']['hits']:
            articles['content'].append(item['_source'])

        return articles

    def query(self, query_str):
        vendors = self.query_vendors(query_str)
        solutions = self.query_solutions(query_str)
        articles = self.query_articles(query_str)
        response = {
            'code': 20000,
            'message': 'success',
            'result': {
                'vendors': vendors,
                'solutions': solutions,
                'articles': articles
            }
        }

        return response

    # 分类别和分页查询
    def query_by_type_and_page(self, body):
        query_str = body['query']
        query_type = body['type']
        offset = body['offset']
        res = self.es.search(
            index=query_type,
            body={
                'from': offset,
                'size': 10,
                '_source': ['url', 'title', 'summary'],
                'query': {
                    'match': {'summary': query_str}
                }
            })
        response = {
            'code': 20000,
            'message': 'success',
            'result': {
                'total': res['hits']['total']['value'],
                'content': []
            }
        }
        for item in res['hits']['hits']:
            response['result']['content'].append(item['_source'])

        return response

    # 节点名称模糊匹配
    def fuzzy_matching(self, title):
        # 之所写了这么多个if，是为了设定模糊匹配时查找的节点类型的优先级
        res = self.es.search(
            index='fintech',
            body={
                '_source': ['title'],
                'query': {
                    'match': {'title': title}
                }
            })
        if res['hits']['total']['value'] == 0:
            res = self.es.search(
                index='vendor',
                body={
                    '_source': ['title'],
                    'query': {
                        'match': {'title': title}
                    }
                })

        if res['hits']['total']['value'] == 0:
            res = self.es.search(
                index='solution',
                body={
                    '_source': ['title'],
                    'query': {
                        'match': {'title': title}
                    }
                })

        if res['hits']['total']['value'] == 0:
            res = self.es.search(
                index='article',
                body={
                    '_source': ['title'],
                    'query': {
                        'match': {'title': title}
                    }
                })
        if res['hits']['total']['value'] == 0:
            return None
        return res['hits']['hits'][0]['_source']['title']

    def match_nodes(self, key_words):
        matched_nodes = []

        if len(key_words[0]) != 0:
            target_vendor = ''.join(key_words[0])
            res = self.es.search(
                index='vendor',
                body={
                    '_source': ['title'],
                    'query': {
                        'match': {'title': target_vendor}
                    }
                })
            if res['hits']['total']['value'] == 0:
                matched_nodes.append('')
            else:
                matched_nodes.append(res['hits']['hits'][0]['_source']['title'])
        else:
            matched_nodes.append('')

        if len(key_words[1]) != 0:
            target_solution = ''.join(key_words[1])
            res = self.es.search(
                index='solution',
                body={
                    '_source': ['title'],
                    'query': {
                        'match': {'title': target_solution}
                    }
                })
            if res['hits']['total']['value'] == 0:
                matched_nodes.append('')
            else:
                matched_nodes.append(res['hits']['hits'][0]['_source']['title'])
        else:
            matched_nodes.append('')

        if len(key_words[2]) != 0:
            target_article = ''.join(key_words[2])
            res = self.es.search(
                index='article',
                body={
                    '_source': ['title'],
                    'query': {
                        'match': {'title': target_article}
                    }
                })
            if res['hits']['total']['value'] == 0:
                matched_nodes.append('')
            else:
                matched_nodes.append(res['hits']['hits'][0]['_source']['title'])
        else:
            matched_nodes.append('')

        return matched_nodes
