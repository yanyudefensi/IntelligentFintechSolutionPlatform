from kg.neo_client import NeoClient
from kg.utils import process_query_entity
from kg.utils import process_find_relation_by_entities


def test1():
    client = NeoClient()
    res = client.query_entity('YonghongX-Suite')
    data, links = process_query_entity(res)
    print('data')
    print(data)
    print('links')
    print(links)


def test2():
    client = NeoClient()
    res = client.find_relation_by_entities('蚂蚁金融科技', 'YonghongX-Suite')
    res = process_find_relation_by_entities(res)
    print(res)


if __name__ == '__main__':
    a = [{
      'name': '区块链清分管理系统',
      'category': 0
    }, {
      'name': '区块链',
      'category': 1
    }, {
      'name': '众享比特',
      'category': 0
    }, {
      'name': '区块链清分管理系统',
      'category': 1
    }, {
      'name': '区块链',
      'category': 0
    }, {
      'name': '众享比特',
      'category': 1
    }, {
      'name': '区块链',
      'category': 0
    }, {
      'name': '蚂蚁金融科技',
      'category': 1
    }]
    print(a.remove({
      'name': '区块链清分管理系统',
      'category': 0
    }))
