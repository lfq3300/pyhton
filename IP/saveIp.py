#存储IP 连接redis
import redis
from random import choice
MAX_SCORE = 100 #最大权重
MIN_SCORE = 0 #最小权重
INIT_SCORE = 10 #初始化权重
REDIS_PORT = 6379 #redis端口
REDIS_HOST = '120.79.247.219' #redis地址
REDIS_USER = 'root'
REDIS_PASSWORD = 'foobared' # redis 密码
REDIS_KEY = 'proxiesip' #redis key
class RedisClient(object):
    def __init__(self,host=REDIS_HOST,port=REDIS_PORT,pwd=REDIS_PASSWORD):
        self.db = redis.StrictRedis(host=host,port=port,password=pwd)

    def add(self,proxy,score=INIT_SCORE):
        '''
        添加代理
        :param proxy:代理
        :param score:分数
        :return:添加结果
        '''
        if not self.db.zscore(proxy,score):
            return self.db.zadd(REDIS_KEY,score,proxy)

    def delete(self,proxy):
        '''
        :param proxy: 删除代理
        '''
        self.db.zrem(REDIS_KEY,proxy)

    def getRanDom(self):
        '''
        获取随机代理IP 根据score权重从大到小进行排序
        :return:
        '''

        '''
        zrangebyscore 对应的 zadd 中的score进行排序   zrangebyscore(name,min,max) 可以指定一个范围  获取score在 min-nax范围的切片
        '''
        result = self.db.zrangebyscore(REDIS_KEY,MAX_SCORE,MAX_SCORE)
        if len(result):
            return choice(result)
        else:
            '''
            zrevrange 根据 score 从大到小排序  然后 0-100指定区间范围 
            '''
            result = self.db.zrevrange(REDIS_KEY,0,100)
            if len(result):
                return choice(result)
            else:
                return  None

    def decrease(self, proxy):
        '''
        代理权重-1 减到 0 就删除
        :param proxy:
        :return:
        '''
        score = self.db.zscore(REDIS_KEY,proxy)
        if score and score> MIN_SCORE:
            '''代理当前权重-1'''
            return  self.db.zincrby(REDIS_KEY,proxy,-1)
        else:
            '''删除代理'''
            return  self.db.zrem(REDIS_KEY,proxy)

    def max(self,proxy):
        '''
        将代理设置为max
        :return:
        '''
        return self.db.zadd(REDIS_KEY,MAX_SCORE,proxy)

    def all(self):
        return  self.db.zrangebyscore(REDIS_KEY,MIN_SCORE,MAX_SCORE)
    def count(self):
        return  self.db.zcard(REDIS_KEY)

if __name__ == '__main__':
    r = RedisClient();
