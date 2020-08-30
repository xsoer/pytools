from nltk.tokenize import sent_tokenize
import jieba
from collections import Counter

para = ""

with open('doc/t1.txt', encoding='utf-8') as f:
    content = f.readlines()
    for s in content:
        s = s.strip().strip('\n')
        if s:
            para += s
            # print(s)
            # print(list(jieba.cut(s, True)))
            # for a in jieba.cut(s, True):
            #     print(a)

# print(Counter(list(jieba.cut(para, True))))

counter = Counter(list(jieba.cut(para, True)))

print(counter)

# print(sent_tokenize(para))
# for a in jieba.cut(para, True):
#     print(a)
