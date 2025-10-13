
import threading
import queue

class Node:
    def __init__(self, key:int, value:int):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class DLL:
    def __init__(self):
        self.head = None
        self.tail = None


    def makeHead(self,node: Node):
        return None

    def addHead(self,node:Node):
        return None

    def remove(self, node:Node):
        return None

    def makeTail(self,node:Node):
        return None

    def addTail(self,node:Node):
        return None


class LRUCache:
    def __init__(self,capacity: int):
        self.capacity = capacity
        self.cache_dict = {}
        self.cache_dll = None
        self.tlock = threading.Lock()

    def get(self,key: int):
        return -1

    def put(self,key:int, value:int):
        return None


class NWaySetAssociateCache:
    def __init__(self, no_sets:int, no_ways: int, replace_policy: str):
        self.no_sets = no_sets
        self.no_ways = no_ways
        self.replace_policy = replace_policy

    def getSetNo(self,key: int):

        return hash(key) % self.no_sets



if __name__ == '__main__':
    no_sets = 2
    no_ways = 3
    no_threads = 1

    actions = []


