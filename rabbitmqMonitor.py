import pika
import time
import json
#监听
import redis

# 定义一个回调函数来处理消息队列中的消息，
def callback(ch, method, properties, body):
    ch.basic_ack(delivery_tag = method.delivery_tag)
    #time.sleep(5)
    saveInRedis(body.decode())
    print(body.decode())

def init(queueName):
    credentials = pika.PlainCredentials('guest', 'guest')
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='139.159.209.32', port=5672, virtual_host='/', credentials=credentials))
    channel = connection.channel()
    # 告诉rabbitmq，用callback来接收消息
    channel.basic_consume(queueName, callback)
    # 开始接收信息，并进入阻塞状态，队列里有信息才会调用callback进行处理
    channel.start_consuming()

def saveInRedis(s):
    js = json.loads(s)
    if(js['password']==''or js['mail']==''or js['id']==''):
        print("无效")
    else:
        print("有效")

    r = redis.Redis(host='127.0.0.1', port=6379, db=1, password=None, decode_responses=True)
    r.hset("account",js['id'],s)
    print(r.hgetall("account"))


