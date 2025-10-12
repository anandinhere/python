from collections import deque
class LRUCache:

    def __init__(self, capacity: int):
        self.cache_dict = {}
        self.cache_dq = deque()
        self.capacity = capacity
        print(f'''capacity {capacity}''')


    # if found in cache, make head and return Value
    # if not found in cache, return -1
    def get(self, key: int) -> int:
        print(f'''get {key} , {self.cache_dict.keys()}''')
        #self.cache_dll.printdll()
        if key in self.cache_dict:
            node = self.cache_dict[key]
            self.cache_dq.remove(node)
            self.cache_dq.appendleft(node)
            return self.cache_dict[key].val
        else:
            return -1


    # if cache is full
    #   found in cache? bring it to head. not found in cache? make it head, remove tail(if put)
    # if cache is not full
    #   found in cache? bring it to head. not found in cache? make it head
    def put(self, key: int, value: int) -> None:
        print(f'''put {key} , {self.cache_dict.keys()}''')
        #self.cache_dll.printdll()
        if len(self.cache_dict) == self.capacity:
            if key in self.cache_dict:
                node = self.cache_dict[key]
                node.val = value
                self.cache_dq.remove(node)
                self.cache_dq.appendleft(node)
                self.cache_dict.update({key: node})
            else:
                node = Node(key, value)
                tail = self.cache_dq[-1]
                self.cache_dq.remove(tail)
                self.cache_dq.appendleft(node)
                self.cache_dict.pop(tail.key)
                self.cache_dict.update({key: node})

        else:
            if key in self.cache_dict:
                node = self.cache_dict[key]
                node.val = value
                self.cache_dq.remove(node)
                self.cache_dq.appendleft(node)
                self.cache_dict.update({key: node})
            else:
                node = Node(key, value)
                self.cache_dq.appendleft(node)
                self.cache_dict.update({key: node})


class Node:
    def __init__(self, key:int, val: int, left: 'Node' = None, right: 'Node' = None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right