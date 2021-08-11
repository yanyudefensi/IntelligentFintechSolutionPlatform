import jieba
import jieba.posseg


class KeyWordExtract():
    def __init__(self):
        self.stopwords = [line.strip() for line in
                     open('../resource/stopwords.txt', encoding='utf-8-sig').readlines()]  # 加载停用词
        self.vendor = [line.strip() for line in open('../resource/vendor.txt', encoding='utf-8-sig').readlines()]  # 加载供应商词典
        jieba.load_userdict('../resource/user_dict.txt')  # 加载用户自定义词典

    def extract(self, s):
        n = ['n', 'nr', 'nr1', 'nr2', 'nrj', 'nrf', 'ns', 'nsf', 'nt', 'nz', 'nl', 'ng', 'x', 'nrt']
        # 根据关键词【方案，服务，业务，功能】判断属于技术文章还是解决方案
        key1 = s.rfind('方案')
        key2 = s.rfind('服务')
        key3 = s.rfind('业务')
        key4 = s.rfind('功能')
        arr = [[], [], []]
        # 依次对每个关键词进行判断
        if key1 != -1:
            s1 = s[:key1 + 2]
            s2 = s[key1 + 2:]
            seg1 = jieba.posseg.cut(s1)
            for word in seg1:
                if word.word not in self.stopwords and word.flag in n:
                    # 如果分词结果属于供应商则添加到arr[0],否则添加到解决方案arr[1]
                    flag = 0
                    for item in self.vendor:
                        if item.find(word.word) != -1:
                            arr[0].append(word.word)
                            flag = 1
                            break
                    if flag == 0:
                        arr[1].append(word.word)
            arr[0] = list(set(arr[0]))
            arr[1] = list(set(arr[1]))
            seg2 = jieba.posseg.cut(s2)
            for word in seg2:
                if word.word not in self.stopwords and word.flag in n:
                    arr[2].append(word.word)
            arr[2] = list(set(arr[2]))
        if key2 != -1:
            s1 = s[:key2 + 2]
            s2 = s[key2 + 2:]
            seg1 = jieba.posseg.cut(s1)
            for word in seg1:
                if word.word not in self.stopwords and word.flag in n:
                    if word.word in self.vendor:
                        arr[0].append(word.word)
                    else:
                        arr[1].append(word.word)
            arr[0] = list(set(arr[0]))
            arr[1] = list(set(arr[1]))
            seg2 = jieba.posseg.cut(s2)
            for word in seg2:
                if word.word not in self.stopwords and word.flag in n:
                    arr[2].append(word.word)
            arr[2] = list(set(arr[2]))
        if key3 != -1:
            s1 = s[:key3 + 2]
            s2 = s[key3 + 2:]
            seg1 = jieba.posseg.cut(s1)
            for word in seg1:
                if word.word not in self.stopwords and word.flag in n:
                    if word.word in self.vendor:
                        arr[0].append(word.word)
                    else:
                        arr[1].append(word.word)
            arr[0] = list(set(arr[0]))
            arr[1] = list(set(arr[1]))
            seg2 = jieba.posseg.cut(s2)
            for word in seg2:
                if word.word not in self.stopwords and word.flag in n:
                    arr[2].append(word.word)
            arr[2] = list(set(arr[2]))
        if key4 != -1:
            s1 = s[:key4 + 2]
            s2 = s[key4 + 2:]
            seg1 = jieba.posseg.cut(s1)
            for word in seg1:
                if word.word not in self.stopwords and word.flag in n:
                    if word.word in self.vendor:
                        arr[0].append(word.word)
                    else:
                        arr[1].append(word.word)
            arr[0] = list(set(arr[0]))
            arr[1] = list(set(arr[1]))
            seg2 = jieba.posseg.cut(s2)
            for word in seg2:
                if word.word not in self.stopwords and word.flag in n:
                    arr[2].append(word.word)
            arr[2] = list(set(arr[2]))
        # 如果输入语句不包含关键词，则认为是技术文章或者供应商
        if key1 == -1 and key2 == -1 and key3 == -1 and key4 == -1:
            seg = jieba.posseg.cut(s)
            for word in seg:
                if word.word not in self.stopwords and word.flag in n:
                    if word.word in self.vendor:
                        arr[0].append(word.word)
                    else:
                        arr[2].append(word.word)
        return arr
