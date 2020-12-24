import redis

client=redis.Redis(host='localhost',password='')
def counter(video_id: int):
    client.set(str(video_id),0,nx=True)
    client.incr(str(video_id))
    print(client.get(str(video_id)).decode())

client.delete(1001)
client.delete(1002)
counter(1001) 
counter(1001)
counter(1002) 
counter(1001) 
counter(1002) 



