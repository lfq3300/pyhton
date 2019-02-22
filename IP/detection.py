'''检测当前IP是否有作用'''

VALID_STATUS_CODES = [200]
TEST_URL = 'http://baidu.com'
BATCH_TEST_SIZE = 100
from IP import saveIp as redisIp
import aiohttp
import asyncio
import time
class Teste(object):
    def __init__(self):
        self.redis = redisIp.RedisClient();

    async def test_single_proxy(self,proxy):
        '''
        检测单个代理
        :param proxy:
        :return:
        '''
        conn = aiohttp.TCPConnector(verify_ssl=False)
        async with aiohttp.ClientSession(connector=conn) as session:
            try:
                if isinstance(proxy,bytes):
                    proxy = proxy.decode('utf-8')
                real_proxy = 'http://'+ proxy
                async with session.get(TEST_URL,proxy=real_proxy,timeout=15) as response:
                    if response.status in VALID_STATUS_CODES:
                        self.redis.max(proxy)
                        print(proxy+"------success")
                    else:
                        self.redis.decrease(proxy)
                        print(proxy+"------error")
            except Exception as e:
                print(e)

    def run(self):
        '''
        测试主函数
        :return:
        '''
        print("浏览器开始运行")

        try:
            proxies = self.redis.all()
            loop = asyncio.get_event_loop() # get_event_loop：创建一个事件循环
            for i in  range(0,len(proxies),BATCH_TEST_SIZE): #range （start,end,[step]）  区间范围 个区间个数
                test_proxies = proxies[i:i + BATCH_TEST_SIZE] # python写法 arr[1:1]
                tasks = [self.test_single_proxy(proxy) for proxy in test_proxies]
                loop.run_until_complete(asyncio.wait(tasks)) #run_until_complete将协程注册到事件循环，并启动事件循环
                time.sleep(5)
        except Exception as e:
            print(e)
            print("浏览器发生错误")

if __name__ == '__main__':
    t = Teste()
    t.run()