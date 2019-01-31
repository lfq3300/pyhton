from bs4 import BeautifulSoup
import requests
url = "https://maoyan.com/board/4?offset=10"
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
}
res = requests.get(url, headers=headers, timeout=20)
html = '';
if res.status_code == 200:
    html = res.text
soup = BeautifulSoup(html,'lxml')

#print(soup.prettify())

# soup.tag.string   tag 属性
print(soup.title.string)

# 获取属性值  也可以指定 attrs['name']
print(soup.p.attrs)

# 可嵌套选择
print(soup.div.p.string)
#contents 返回直接子节点    但是没有返回节点下的 子节点

#print(soup.div.contents)


#children 子节点

print(soup.div.children)
for i,child in enumerate(soup.div.children):
    #print(i,child)
    pass

# 子孙节点

print(soup.div.descendants)

for i,child in enumerate(soup.div.descendants):
    #print(i,child)
    pass

# 父节点 parent

#全部父节点 parents

#兄弟节点 next_sibling  previous_siblings

#find_all 根据节点名称查询  id 和 class(class_) 可以直接查询

# rint(soup.find_all(name='a'))

#根据节点属性查

#print(soup.find_all(attrs={'class':'star'}))


#class 选择器   select

print(soup.select(".star"))