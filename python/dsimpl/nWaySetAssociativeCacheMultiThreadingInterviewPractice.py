
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
        self.remove(node)
        self.addHead(node)

    def makeTail(self,node:Node):
        self.remove(node)
        self.addTail(node)

    def addHead(self,node:Node):
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            old_head = self.head
            node.next = old_head
            old_head.prev = node
            self.head = node


    def addTail(self,node:Node):
        if self.tail is None:
            self.tail = node
            self.head = node
        else:
            old_tail = self.tail
            node.prev = old_tail
            old_tail.next = node
            self.tail = node

    def remove(self, node: Node):

        if self.head is None and self.tail is None:
            return

        if node == self.head and node == self.tail:
            self.head = None
            self.tail = None
        elif node == self.head:
            new_head = node.next
            new_head.prev = None
            self.head = new_head
        elif node == self.tail:
            new_tail = node.prev
            new_tail.next = None
            self.tail = new_tail
        else:
            next = node.next
            prev = node.prev
            next.prev = prev
            prev.next = next


class LRUCache:
    def __init__(self,capacity: int):
        self.capacity = capacity
        self.cache_dict = {}
        self.cache_dll = DLL()
        self.tlock = threading.Lock()


    def printCache(self):
        for key, node in self.cache_dict.items():
            print(f"{key}:{node.value}",end=' ,')
        print()

        node = self.cache_dll.head
        while node:
            print(f"{node.key},{node.value}",end=' -> ')
            node = node.next
        print()


    def get(self,key: int):
        print(f"get {key}")
        if key in self.cache_dict:
            node = self.cache_dict[key]
            self.cache_dll.makeHead(node)
            self.printCache()
            return node.value
        self.printCache()
        return -1

    def put(self,key:int, value:int):
        print(f"put {key}:{value}")
        if len(self.cache_dict) == self.capacity:
            if key in self.cache_dict:
                node = self.cache_dict[key]
                node.value = value
                self.cache_dll.makeHead(node)
                self.cache_dict.update({key:node})
            else:
                tail = self.cache_dll.tail
                self.cache_dll.remove(tail)
                node = Node(key,value)
                self.cache_dict.pop(tail.key)
                self.cache_dict.update({key:node})
                self.cache_dll.addHead(node)
        else:
            if key in self.cache_dict:
                node = self.cache_dict[key]
                node.value = value
                self.cache_dll.makeHead(node)
                self.cache_dict.update({key:node})
            else:
                node = Node(key,value)
                self.cache_dict.update({key:node})
                self.cache_dll.addHead(node)
        self.printCache()

        return None


class NWaySetAssociateCache:
    def __init__(self, no_sets:int, no_ways: int, replace_policy: str):
        self.no_sets = no_sets
        self.no_ways = no_ways
        self.replace_policy = replace_policy
        self.nWayCache = [LRUCache(no_ways) if replace_policy == 'LRU' else None for _ in range(no_sets)]

    def getSetNo(self,key: int):
        return hash(key) % self.no_sets

    def get(self,key: int):
        cacheSetIndex = self.getSetNo(key)
        cacheSet = self.nWayCache[cacheSetIndex]
        with cacheSet.tlock:
            return cacheSet.get(key)

    def put(self, key: int, value: int):
        cacheSetIndex = self.getSetNo(key)
        cacheSet = self.nWayCache[cacheSetIndex]
        with cacheSet.tlock:
            cacheSet.put(key,value)



if __name__ == '__main__':
    no_sets = 1
    no_ways = 3
    no_threads = 1
    replacement_policy = 'LRU'

    actions = [('put',(1,1)),('put',(2,2)),('put',(3,3)),('put',(3,4)),('put',(4,4)),
               ('get',1),('get',2),('get',3),('get',4),('get',5),
               ('put',(5,5)),('put',(1,2))]

    action_q = queue.Queue()
    for action in actions:
        action_q.put(action)

    nWayCache = NWaySetAssociateCache(no_sets,no_ways,replacement_policy)

    def worker():
        while True:
            task = action_q.get()
            item = task[1]
            if task[0] == 'get':
                print(nWayCache.get(item))
            else:
                nWayCache.put(item[0],item[1])

            action_q.task_done()

    for i in range(no_threads):
        worked_thread = threading.Thread(target=worker,daemon=True)
        worked_thread.start()


    action_q.join()


