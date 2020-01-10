import redis
r = redis.Redis(host='127.0.0.1', port=6379, db=1, password=None, decode_responses=True)
list=[1,2,3,]
r.lpush("t",5)
print(r.lindex("t",0))
