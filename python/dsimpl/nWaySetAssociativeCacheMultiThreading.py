'''

nWayCache


-----------
block size is given
    this gives offset size

main memory size is given
    compute total bit count from this

cache size is given
    find total blocks with this and block size

number of ways is given - this is set size

total blocks = C/B
set count = (total cache size)/(block size x number of ways)

index size = log(S)


In direct mapping S = C/B
In fully associative cache S = 1

main memory - tag | index | offset
cache line/entry - tag | data block | flag bits
-----------



List of Lrucache
    length = no of sets/LRUCaches
    LRUcache
        Dict
        DLL
        Capacity = no of ways




'''

import threading
import queue

class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.next = None
        self.previous = None

class DLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def addHead(self,node: Node) -> None:
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            new_head = node
            old_head = self.head
            old_head.previous = new_head
            new_head.next = old_head
            self.head = new_head

    def addTail(self, node: Node) -> None:
        if self.tail is None:
            self.tail = node
            self.head = node
        else:
            new_tail = node
            old_tail = self.tail
            new_tail.previous = old_tail
            old_tail.next = new_tail
            self.tail = new_tail
        return None

    def remove(self, node: Node) -> None:
        if node == self.head and self.head == self.tail:
            self.head = None
            self.tail = None
            return
        if node == self.head:
            self.removeHead()
        elif node == self.tail:
            self.removeTail()
        else:
            prev = node.previous
            next = node.next
            prev.next = next
            next.previous = prev
        return None

    def makeHead(self,node: Node):
        self.remove(node)
        self.addHead(node)

    def removeHead(self):
        head = self.head
        next = head.next
        if next:
            next.previous = None
            self.head = next
        else:
            self.head = None
            self.tail = None

    def makeTail(self, node: Node):
        self.remove(node)
        self.addTail(node)

    def removeTail(self):
        tail = self.tail
        prev = tail.previous
        if prev:
            prev.next = None
            self.tail = prev
        else:
            self.head = None
            self.tail = None


class LRUCache:
    def __init__(self, capacity: int):
        self.cache_dict = {}
        self.cache_dll = DLL()
        self.capacity = capacity
        self.tlock = threading.Lock()


    def printCache(self):
        for key, node in self.cache_dict.items():
            print(f'{key}:{node.value}', end=',')
        print()

        node = self.cache_dll.head
        while node:
            print(f'{node.key}:{node.value}', end='->')
            node = node.next
        print()


    def get(self, key: int) -> int:
        #print(key)

        if key in self.cache_dict:
            node = self.cache_dict[key]
            self.cache_dll.makeHead(node)
            self.printCache()
            return node.value
        else:
            self.printCache()
            return -1

    def put(self, key: int, value: int) -> None:
        #print(f'{key} , {value}')
        #self.printCache()
        if len(self.cache_dict) == self.capacity:
            if key in self.cache_dict:
                node = self.cache_dict[key]
                node.value = value
                self.cache_dll.makeHead(node)
                self.cache_dict.update({key: node})
            else:
                node = Node(key,value)
                tail_key = self.cache_dll.tail.key
                self.cache_dll.removeTail()
                self.cache_dict.pop(tail_key)
                self.cache_dll.addHead(node)
                self.cache_dict.update({key: node})
        else:
            if key in self.cache_dict:
                node = self.cache_dict[key]
                node.value = value
                self.cache_dll.makeHead(node)
                self.cache_dict.update({key: node})
            else:
                node = Node(key,value)
                self.cache_dll.addHead(node)
                self.cache_dict.update({key: node})

        self.printCache()


class MRUCache(LRUCache):
     def get(self, key: int):
         return None

     def put(self, key: int, value: int):
         return None




class NWaySetCache:
    def __init__(self, no_sets : int, no_ways: int, cache_type: str):
        self.no_sets = no_sets
        self.sets = [LRUCache(no_ways) for _ in range(no_sets)] if cache_type == 'LRU' \
            else [MRUCache(no_ways) for _ in range(no_sets)]
        self.no_ways = no_ways

    def get(self, key: int):

        setIndex = self.getSetIndex(key)
        setCache = self.sets[setIndex]
        with setCache.tlock:
            print(f"get  {key}")
            return setCache.get(key)

    def getSetIndex(self,key):

        return hash(key) % self.no_sets

    def put(self, key: int, value: int):
        setIndex = self.getSetIndex(key)
        setCache = self.sets[setIndex]
        with setCache.tlock:
            print(f"put  {key},{value}")
            return setCache.put(key,value)






if __name__ == '__main__':
    task_queue = queue.Queue()

    actions = [ ('put', (1,1)) , ('put', (2,2)), ('put', (3,3)), ('put', (4,4)), ('put', (5,5)),
                ('get', 1), ('get', 2), ('get', 3), ('get', 1), ('get', 5),
                ('put', (1,1)), ('put', (1,1))]

    no_of_worker_threads = 1
    no_of_sets = 2
    no_of_ways = 2
    replacement_policy = 'LRU'

    nWaySetCache = NWaySetCache(no_of_sets,no_of_ways,replacement_policy)

    def worker(name):
        while True:
            #print(f"thread - {name}")
            task = task_queue.get()
            if task is None:
                break

            action, item = task[0], task[1]


            if action == 'get':
                print(nWaySetCache.get(item))
            else:
                nWaySetCache.put(item[0], item[1])

            task_queue.task_done()


    for i in range(no_of_worker_threads):
        thread_name = f"thread={i+1}"
        worker_thread = threading.Thread(target=worker, name=thread_name, args=(thread_name,),daemon=True)
        worker_thread.start()

    for action in actions:
        task_queue.put(action)




    task_queue.join()







