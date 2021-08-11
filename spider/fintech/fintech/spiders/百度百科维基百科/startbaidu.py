import baidu
import baidukeys
import csv

fintech=['区块链','人工智能','云计算','大数据','物联网']
for name in fintech:
    totalkeys=[]
    for i in range(3):
        totalkeys.extend(baidukeys.get_relevant_keys(name))
    totalkeys = list(set(totalkeys))
    totalkeys2 = totalkeys.copy()
    for i in totalkeys:
        totalkeys2.extend(baidukeys.get_relevant_keys(i))
        # print (i)
    totalkeys2 = list(set(totalkeys2))
    length=len(totalkeys2)
    print(length,totalkeys2)
    count=0
    with open('d://'+name+'.csv', 'w', newline='',encoding='utf-8-sig') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(('标题', '摘要', '类型', '内容'))
        for i in totalkeys2:
            print((name+'%.2f'%(count/length*100)) + "%")
            count+=1
            try :
                content = baidu.search(i)
                content.replace("\n", "").replace("\r", "")
                csv_writer.writerow((name, content[:20], '文档', content))
            except:
                pass

