class LRUCache:

    def __init__(self, capacity: int):
        self.cache_dict = {}
        self.cache_dll = DLL()
        self.capacity = capacity


    # if found in cache, make head and return Value
    # if not found in cache, return -1
    def get(self, key: int) -> int:
        if key in self.cache_dict:
            node = self.cache_dict[key]
            self.cache_dll.remove(node)
            self.cache_dll.add_head(node)
            return self.cache_dict[key].val
        else:
            return -1


    # if cache is full
    #   found in cache? bring it to head. not found in cache? make it head, remove tail(if put)
    # if cache is not full
    #   found in cache? bring it to head. not found in cache? make it head
    def put(self, key: int, value: int) -> None:
        if len(self.cache_dict) == self.capacity:
            if key in self.cache_dict:
                node = self.cache_dict[key]
                node.val = value
                self.cache_dll.pop(node)
                self.cache_dll.add_head(node)
            else:
                node = Node(key, value)
                tail = self.cache_dll.tail
                tail_key = tail.key
                self.cache_dict.pop(tail_key)
                self.cache_dll.add_head(node)

        else:
            if key in self.cache_dict:
                node = self.cache_dict[key]
                node.val = value
                self.cache_dll.remove(node)
                self.cache_dll.add_head(node)
            else:
                node = Node(key, value)
                self.cache_dll.add_head(node)


class Node:
    def __init__(self, key:int, val: int, left: 'Node' = None, right: 'Node' = None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right


class DLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    # head <> second <> tail

    def add_head(self, node :Node):
        head = self.head
        node.right = self.head
        head.left = node
        self.head = node


    def add_tail(self,node:Node):
        tail = self.tail
        node.left = self.tail
        tail.right = node
        self.tail = node


    def remove(self, node : Node = None):
        left = node.left
        right = node.right

        if node == self.head:
            head = self.head
            second = node.right
            self.head = second
            second.left = None
        elif node == self.tail:
            tail = self.tail
            second = node.left
            self.tail = second
            second.right = None
        else:
            left = node.left
            right = node.right
            left.right = right
            right.left = left











        # Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)