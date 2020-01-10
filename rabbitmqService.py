# 发送信息
import json

import pika

def send(exchange,routingkey,msg):
    credentials = pika.PlainCredentials('guest', 'guest')  # mq用户名和密码
    # 虚拟队列需要指定参数 virtual_host，如果是默认的可以不填。
    connection = pika.BlockingConnection(pika.ConnectionParameters(host = '139.159.209.32',port = 5672,virtual_host = '/',credentials = credentials))
    channel=connection.channel()
    # 向队列插入数值 routing_key是队列名
    channel.basic_publish(exchange = exchange,routing_key = routingkey,body = msg)
    print(msg)
    connection.close()