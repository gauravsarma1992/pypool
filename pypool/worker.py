from multiprocessing import Queue
from typing import Callable


class Callback:
    def __init__(self, func: Callable):
        self.callable: "Callable" = func


class Worker:
    def __init__(self, id: str, ):
        self.id: str = id
        self.queue: "Queue" = Queue()

    def process(self):
        pass