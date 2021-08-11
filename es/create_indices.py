from elasticsearch import Elasticsearch

es = Elasticsearch(hosts=[{'host': 'localhost', 'port': 9000}])

res1 = es.indices.create(
    index='solution',
    ignore=400,
    body={
        'settings': {
            'number_of_shards': 3,
            'number_of_replicas': 2
        },
        'mappings': {
            'properties': {
                'type': {'type': 'integer'},
                'url': {'type': 'text'},
                'title': {'type': 'text'},
                'summary': {'type': 'text'},
                'content': {'type': 'text'},
                'vendor': {'type': 'text'}
            }
        }
    }
)
print(res1)

res2 = es.indices.create(
    index='article',
    ignore=400,
    body={
        'settings': {
            'number_of_shards': 3,
            'number_of_replicas': 2
        },
        'mappings': {
            'properties': {
                'type': {'type': 'integer'},
                'url': {'type': 'text'},
                'title': {'type': 'text'},
                'summary': {'type': 'text'},
                'content': {'type': 'text'}
            }
        }
    }
)
print(res2)

res3 = es.indices.create(
    index='vendor',
    ignore=400,
    body={
        'settings': {
            'number_of_shards': 3,
            'number_of_replicas': 2
        },
        'mappings': {
            'properties': {
                'type': {'type': 'integer'},
                'url': {'type': 'text'},
                'title': {'type': 'text'},
                'summary': {'type': 'text'},
                'content': {'type': 'text'}
            }
        }
    }
)
print(res3)

res4 = es.indices.create(
    index='fintech',
    ignore=400,
    body={
        'settings': {
            'number_of_shards': 3,
            'number_of_replicas': 2
        },
        'mappings': {
            'properties': {
                'title': {'type': 'integer'},
                'summary': {'type': 'text'},
                'content': {'type': 'text'}
            }
        }
    }
)
print(res4)
