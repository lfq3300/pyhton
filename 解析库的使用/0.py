from lxml import etree

text = '<tr><th>1</th><th>2</th><th>3</th><th>4</th><th>5</th>'

html = etree.HTML(text)

result = etree.tostring(html)


html = etree.parse('0.html',etree.HTMLParser())

#单class获取
result = html.xpath("//li[@class='item']/text()")
print(result)

#属性获取
result = html.xpath("//a/@href")
print(result)

# 多class获取
result = html.xpath("//li[@class='item it']/text()")
print(result)

# 还支持 name 等属性 筛选 支持 or and 条件 具体查看文档

# 支持位置筛选  lats() 最后一个 last() - 1 倒数第一个

# 支持父节点 子节点 祖先节点筛选
