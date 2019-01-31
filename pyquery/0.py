from pyquery import PyQuery as pq

doc = pq(url="https://maoyan.com/board/4?offset=10")
print(doc('title'))

#css 选择器

print(doc(".name a"))

#pyjuery 和 jquery的css选择器相同