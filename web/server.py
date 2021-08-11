import sys
sys.path.append('../')

from flask import Flask, jsonify, request
from web.config import config
from es.query import EsQuery
from kg.kg_query import KgQuery
from kg.keyword_extract import KeyWordExtract

app = Flask(__name__)
es_query = EsQuery()
kg_query = KgQuery()
keyword_extract = KeyWordExtract()

@app.route('/search', methods=['POST'])
def query():
    values = request.get_json()
    query_str = values.get('query')
    print('查询条件：', query_str)
    response = es_query.query(query_str)

    return jsonify(response), 200


@app.route('/search/paging', methods=['POST'])
def query_by_type_and_page():
    query_body = request.get_json()
    print('查询体：', query_body)
    response = es_query.query_by_type_and_page(query_body)

    return jsonify(response), 200


@app.route('/kg/entity_query', methods=['POST'])
def entity_query():
    query_body = request.get_json()
    entity = query_body.get('entity')
    match_entity = es_query.fuzzy_matching(entity)
    if match_entity is not None:
        if kg_query.entity_query(match_entity) is not None:
            data, links = kg_query.entity_query(match_entity)
            response = {
                'code': 20000,
                'message': 'success',
                'result': {
                    'data': data,
                    'links': links
                }
            }
            return jsonify(response), 200
        else:
            response = {
                'code': 30001,
                'message': '没有相关实体'
            }
            return jsonify(response), 200
    else:
        response = {
            'code': 30001,
            'message': '没有相关实体'
        }
        return jsonify(response), 200


@app.route('/kg/entity_relation_query', methods=['POST'])
def entity_relation_query():
    query_body = request.get_json()
    entity1 = query_body.get('entity1')
    entity2 = query_body.get('entity2')
    match_entity1 = es_query.fuzzy_matching(entity1)
    match_entity2 = es_query.fuzzy_matching(entity2)
    if match_entity1 is not None and match_entity2 is not None:
        if kg_query.relation_query(match_entity1, match_entity2) is not None:
            data, links = kg_query.relation_query(match_entity1, match_entity2)
            response = {
                'code': 20000,
                'message': 'success',
                'result': {
                    'data': data,
                    'links': links
                }
            }
            return jsonify(response), 200
        else:
            response = {
                'code': 30002,
                'message': '不存在相关关系'
            }
            return jsonify(response), 200
    else:
        response = {
            'code': 30002,
            'message': '不存在相关关系'
        }
        return jsonify(response), 200


@app.route('/kg/intelligent_qa', methods=['POST'])
def intelligent_qa():
    query_body = request.get_json()
    question = query_body.get('question')
    key_words = keyword_extract.extract(question)
    matched_nodes = es_query.match_nodes(key_words)
    if kg_query.intelligent_qa(matched_nodes) is not None:
        tips, data, links = kg_query.intelligent_qa(matched_nodes)
        response = {
            'code': 20000,
            'message': 'success',
            'result': {
                'tips': tips,
                'data': data,
                'links': links
            }
        }
        return jsonify(response), 200
    else:
        response = {
            'code': 40001,
            'message': '很抱歉没有找到相关信息'
        }
        return jsonify(response), 200


if __name__ == '__main__':
    app.run(host=config['host'], port=config['port'])
