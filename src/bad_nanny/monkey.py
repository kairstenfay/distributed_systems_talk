import builtins
import socket
import random
import time


def _maybe_sleep(func, min_time=0, max_time=10000, probability=0.01):
    def _inner(*args, **kwargs):
        if random.random() < probability:
            to_sleep = random.uniform(min_time, max_time)
            time.sleep(to_sleep)
        return func(*args, **kwargs)

    return _inner


def _maybe_raise(func, exception=Exception, probability=0.01):
    def _inner(*args, **kwargs):
        if random.random() < probability:
            raise exception
        return func(*args, **kwargs)

    return _inner


def patch(probability=0.01):
    builtins.open = _maybe_sleep(
        _maybe_raise(
            builtins.open, exception=OSError("Chaos monkey says there is no file system today"), probability=probability
        ),
        probability=probability,
    )
    socket.socket.__init__ = _maybe_sleep(
        _maybe_raise(
            socket.socket.__init__,
            exception=OSError("Chaos monkey says there is no network today"),
            probability=probability,
        ),
        probability=probability,
    )
