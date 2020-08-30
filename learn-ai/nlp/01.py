import jieba
import jieba.analyse
from collections import Counter

f = open('data/硅谷禁书.txt', encoding='utf-8')
content = f.read()
f.close()

print("总字数--->", len(content))

rsp = jieba.cut(content)
print(Counter(rsp))

# for r in rsp:
#     print(r)


top20 = jieba.analyse.extract_tags(content, withWeight=True)
# print(top20)
for word in top20:
    print(word)

