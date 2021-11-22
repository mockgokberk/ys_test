import json
import redis


class RedisClient():
    def __init__(self):
        self.redis_client = redis.StrictRedis(host='redis', port=6379, db=1)

    def get_client(self):
        return self.redis_client

    def publish_data_on_redis(self, json_data, channel_name):
        self.redis_client.publish(channel_name, json.dumps(json_data))
        return True
