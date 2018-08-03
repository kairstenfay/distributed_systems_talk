import redis


class Semaphore:
    def __init__(self, name, host, port):
        self._name = name
        self._redis = redis.Redis(host=host, port=port)

    def add_dependencies(self, *dependency_ids):
        print("Adding dependencies.")
        for dependency_id in dependency_ids:
            self._redis.sadd(self._name, dependency_id)

    def clear_dependencies(self, *dependency_ids):
        print("Clearing dependencies.")
        for dependency_id in dependency_ids:
            self._redis.srem(self._name, dependency_id)

    def is_clear(self):
        return self._redis.scard(self._name) == 0
