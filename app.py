import redis
import datetime
import json

r = redis.Redis()

username = False

while True:
    if not username:
        username = input("Please type your name: ")
    body = input("Start typing: ")

    if body == 'exit':
        username = False
        break
    elif body == 'user':
        username = input("Please type your name: ")
        continue

    message = {
        "username": username,
        "body": body,
        "timestamp": str(datetime.datetime.utcnow())
    }

    transport_msg = json.dumps(message)

    r.lpush('my-new-history', transport_msg)

    r.publish('new-chat', transport_msg)
