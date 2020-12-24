import redis
import time

client=redis.Redis(host='localhost',password='',decode_responses=True)

def sendsms(telephone_number: int, content: str, key=None):
    # 短信发送逻辑, 作业中可以使用 print 来代替
    client.set(telephone_number,0,nx=True,ex=60)
    client.incr(telephone_number)
    if int(client.get(telephone_number))<=5:
        print('发送成功')
    else:
        print(' 1 分钟内发送次数超过 5 次, 请等待 1 分钟')

while True:
    time.sleep(1)
    sendsms(12345654321, content="hello")
