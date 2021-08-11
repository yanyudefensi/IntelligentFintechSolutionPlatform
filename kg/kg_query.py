from kg.neo_client import NeoClient
from kg.utils import process_query_entity
from kg.utils import process_find_relation_by_entities
from kg.utils import process_relation_amount_three

class KgQuery():
    def __init__(self):
        self.client = NeoClient()

    def entity_query(self, entity):
        row = self.client.query_entity(entity)
        data, links = process_query_entity(row)
        if len(data) > 0 and len(links) > 0:
            return data, links
        else:
            return None

    def relation_query(self, entity1, entity2):
        row = self.client.find_relation_by_entities(entity1, entity2)
        data, links = process_find_relation_by_entities(row)
        if len(data) > 0 and len(links) > 0:
            return data, links
        else:
            return None

    def intelligent_qa(self, nodes):
        count = 0
        indices = []
        for index, item in enumerate(nodes):
            if item != '':
                count += 1
                indices.append(index)

        if count == 0:
            return None
        elif count == 1:
            print(nodes[indices[0]])
            data, links = self.entity_query(nodes[indices[0]])
            tips = f'您是不是想找：{nodes[indices[0]]}'
            return tips, data, links
        elif count == 2:
            relation = self.relation_query(nodes[indices[0]], nodes[indices[1]])
            if relation is not None:
                tips = f'您是不是想找：{nodes[indices[0]]} 和 {nodes[indices[1]]}'
                data, links = self.relation_query(nodes[indices[0]], nodes[indices[1]])
                return tips, data, links

            else:
                entity1 = self.entity_query(nodes[indices[0]])
                if entity1 is not None:
                    tips = f'您是不是想找：{nodes[indices[0]]}'
                    data, links = self.entity_query(nodes[indices[0]])
                    return tips, data, links

                entity2 = self.entity_query(nodes[indices[1]])
                if entity2 is not None:
                    tips = f'您是不是想找：{nodes[indices[1]]}'
                    data, links = self.entity_query(nodes[indices[1]])
                    return tips, data, links

                return None
        else:
            state, row = self.client.find_relation_amount_three(nodes)
            tips = f'您想找的是和这个供应商：{nodes[indices[0]]}  相关的所有信息吗？'
            data, links = process_relation_amount_three(state, row)
            return tips, data, links
