import weki
import wekikeys
import csv

fintech=['Big data','Artificial intelligence','Cloud computing','Internet of things']
for name in fintech:
    totalkeys=[]
    for i in range(3):
        totalkeys.extend(wekikeys.get_relevant_keys(name))
    totalkeys = list(set(totalkeys))
    totalkeys2 = totalkeys.copy()
    for i in totalkeys:
        totalkeys2.extend(wekikeys.get_relevant_keys(i))
        # print (i)
    totalkeys2 = list(set(totalkeys2))
    length=len(totalkeys2)
    print(length,totalkeys2)
    count=0
    with open('D://'+name+'.csv', 'w', newline='',encoding='utf-8-sig') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(('标题', '摘要', '类型', '内容'))
        for i in totalkeys:
            print((name+'%.2f'%(count/length*100)) + "%")
            count+=1
            try :
                content=weki.search(i)
                content.replace("\n", "").replace("\r","")
                # print(content)
                csv_writer.writerow((name, content[:20], '文档', content))
            except:
                pass