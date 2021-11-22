import time

import redis
import requests
import json
import urllib3.exceptions
import time

class SendOrders():
    subscriber = redis.Redis(host='redis', port=6379)
    channel = 'orders'
    p = subscriber.pubsub()
    p.subscribe(channel)
    while True:
        message = p.get_message()
        if message and not message['data'] == 1:
            data = json.loads(message['data'].decode('utf-8'))
            try:
                time.sleep(10)
                r = requests.post("http://app:8000/api/v1/order/", data=data)
            except (urllib3.exceptions.NewConnectionError,
                    requests.exceptions.ConnectionError) as e :
                time.sleep(10)
                r = requests.put("http://app:8000/api/v1/order/", data=data)

