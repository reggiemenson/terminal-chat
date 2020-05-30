import time
import redis
import json

r = redis.Redis(decode_responses=True)

p = r.pubsub(ignore_subscribe_messages=True)
p.subscribe('new-chat')

history = r.lrange('my-new-history', 0, 5)

for message in reversed(history):
    message_dict = json.loads(message)
    print(
        f"""{message_dict['username']} - {message_dict['timestamp']}
        \n{message_dict['body']}""",
        '\n'
        )

while True:
    time.sleep(1.10)
    message = p.get_message()
    if message:
        message_dict = json.loads(message['data'])
        print(
            f"""{message_dict['username']} - {message_dict['timestamp']}
            \n{message_dict['body']}""",
            '\n'
        )
