import pymysql

db = pymysql.connect(host='127.0.0.1', user='root', password='root', port=3306, db='pydb')
cursor = db.cursor()
sql = 'INSERT INTO students(name,age) values (%s,%s)'
try:
    cursor.execute(sql,('luo',20))
    db.commit()
except Exception as e:
    db.rollback()
    print(e)


# 动态sql 语句

data = {
    'name':'哈哈哈',
    'age':12
}
table = 'students'
keys = ','.join(data.keys())
values = ','.join(['%s'])*len(data)
print(keys)
print(values)
