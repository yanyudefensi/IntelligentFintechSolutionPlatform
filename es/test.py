from es.query import EsQuery

client = EsQuery()
print(client.fuzzy_matching('蚂蚁金融科技'))