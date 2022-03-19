import aioredis

from typing import Optional
from aioredis import Redis


class RedisManager:
    def __init__(self, password=None):
        self.redis: Optional[Redis] = None
        self._password = password

    async def init_cache(self):
        self.redis = aioredis.Redis.from_url("redis://redis_service", port=6379, decode_responses=True)

    async def keys(self, pattern):
        return await self.redis.keys(pattern)

    async def set(self, key, value, exp=7200):
        return await self.redis.set(key, value, exp)

    async def hset(self, name, mapping):
        return await self.redis.hset(name, mapping=mapping)

    async def lpush(self, name, data):
        return await self.redis.lpush(name, *data)

    async def lrange(self, key_name, start=0, end=-1):
        return await self.redis.lrange(key_name, start, end)

    async def expire_key(self, name, time):
        return await self.redis.expire(name, time)

    async def hget(self, name, key):
        return await self.redis.hget(name, key)

    async def get(self, key):
        return await self.redis.get(key)

    async def is_exists(self, name):
        return await self.redis.exists(name)

    async def close(self):
        await self.redis.сlose()


redis_manager = RedisManager()
