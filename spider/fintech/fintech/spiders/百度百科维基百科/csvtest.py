import csv
# with open('D://test.csv', 'w', newline='',encoding='utf-8-sig') as csv_file:
#     csv_writer = csv.writer(csv_file)
#     csv_writer.writerow(('区块链','类型', '文档', '内容'))

a=[2,3]
b=a.copy()
print (b)
a.extend([1,2])
print (b)
