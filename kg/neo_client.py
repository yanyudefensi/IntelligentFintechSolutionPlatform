from py2neo import Graph, Node, Relationship, cypher, Path


class NeoClient():
    def __init__(self):
        self.graph = Graph("http://114.116.189.184:11000", username="neo4j", password="neo4jpwd")

    # 实体查询
    def query_entity(self, value):
        answer = self.graph.run(
            cypher=
            f'MATCH (entity1:fintech) - [rel] -> (entity2)  '
            f'WHERE entity1.title = "{value}" '
            f'RETURN entity1, rel,entity2 '
            f'LIMIT 25'
        ).data()

        if len(answer) == 0:
            answer = self.graph.run(
                cypher=
                f'MATCH (entity1) - [rel] -> (entity2)  '
                f'WHERE entity1.title = "{value}" '
                f'RETURN entity1, rel,entity2 '
                f'LIMIT 25'
            ).data()

        if len(answer) == 0:
            answer = self.graph.run(
                cypher=
                f'MATCH (entity1) - [rel] -> (entity2)  '
                f'WHERE entity2.title = "{value}" '
                f'RETURN entity1, rel,entity2 '
                f'LIMIT 25'
            ).data()

        return answer

    # 两个实体之间联系的查询
    def find_relation_by_entities(self, entity1, entity2):
        answer = self.graph.run(
            "MATCH"
            + "(p1{title:\""
            + str(entity1) + "\"}),"
            + "(p2{title:\""
            + str(entity2) + "\"}),"
            + "p=shortestpath((p1)-[rel:RELATION*]-(p2)) RETURN rel").evaluate()

        result = []
        if answer is not None:
            for item in answer:
                tmp = {}
                start_node = item.start_node
                end_node = item.end_node
                tmp['start_node'] = start_node
                tmp['relation'] = item
                tmp['end_node'] = end_node
                result.append(tmp)

        return result

    # 三个相关实体之间的查询
    def find_relation_amount_three(self, nodes):
        vendor = nodes[0]
        solution = nodes[1]
        article = nodes[2]

        answer = self.graph.run(
            cypher=
            f'MATCH (entity1:vendor) - [rel1] - (entity2:solution)-[rel2]-(entity3:article)'
            f'WHERE entity1.title ="{vendor}" '
            f'AND entity2.title="{solution}" '
            f'AND entity3.title="{article}" '
            f'RETURN entity1, rel1, entity2, rel2, entity3'
        ).data()

        if len(answer) == 1:
            return 3, answer

        answer = self.find_relation_by_entities(vendor, solution)
        if len(answer) != 0:
            return 2, answer

        answer = self.query_entity(vendor)
        return 1, answer
