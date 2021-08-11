import json


# 处理实体查询时从数据库返回的数据，把数据格式化成前端容易使用的形式
def process_query_entity(row):
    if len(row) > 0:
        json_list = []
        data = []
        links = []

        for item in row:
            json_list.append(json.loads(json.dumps(item, ensure_ascii=False)))

        entity1 = {
            'name': json_list[0].get('entity1').get('title')
        }
        data.append(entity1)

        for item in json_list:
            data.append({
                'name': item.get('entity2').get('title'),
                'category': 1
            })
            links.append({
                'source': entity1.get('name'),
                'target': item.get('entity2').get('title'),
                'category': 0,
                'value': item.get('rel').get('type'),
                'symbolSize': 10
            })

        return data, links
    else:
        return [], []


# 加工关系查询返回的数据
def process_find_relation_by_entities(row):
    if len(row) > 0:
        data = []
        links = []
        for item in row:
            data.append({
                'name': item['start_node']['title'],
                'category': 0
            })
            data.append({
                'name': item['end_node']['title'],
                'category': 1
            })

            links.append({
                'source': item['start_node']['title'],
                'target': item['end_node']['title'],
                'value': item['relation']['type'],
                'symbolSize': 10
            })

        # 对数据节点进行去重
        count = {}
        for index in range(len(data)-1, -1, -1):
            if data[index]['name'] not in count:
                count[data[index]['name']] = 1
            else:
                del data[index]
        print('去重后')
        print(data)

        return data, links
    else:
        return [], []


# 处理实体查询时从数据库返回的数据，把数据格式化成前端容易使用的形式
def process_relation_amount_three(state, row):
    if state == 1:
        return process_query_entity(row)

    elif state == 2:
        return process_find_relation_by_entities(row)

    else:
        result_map = json.loads(json.dumps(row[0], ensure_ascii=False))
        entity1 = {
            'name': result_map.get('entity1').get('title'),
            'category': 0
        }
        entity2 = {
            'name': result_map.get('entity2').get('title'),
            'category': 1
        }
        entity3 = {
            'name': result_map.get('entity3').get('title'),
            'category': 2
        }
        rel1 = {
            'source': entity1.get('name'),
            'target': entity2.get('name'),
            'category': 0,
            'value': result_map.get('rel1').get('type'),
            'symbolSize': 10
        }
        rel2 = {
            'source': entity2.get('name'),
            'target': entity3.get('name'),
            'category': 0,
            'value': result_map.get('rel2').get('type'),
            'symbolSize': 10
        }

        data = [entity1, entity2, entity3]
        links = [rel1, rel2]

        return data, links


