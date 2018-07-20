import redis


class Semaphore:
    def __init__(self, name, host, port):
        self._name = name
        self._redis = redis.Redis(host=host, port=port)

    def add_dependencies(self, job_ids):
        self._redis.sadd(self._name, *job_ids)

    def clear_dependency(self, job_id):
        self._redis.srem(self._name, job_id)

    def is_clear(self):
        return self._redis.scard(self._name) == 0
