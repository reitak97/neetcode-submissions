class ListNode():
    def __init__(self,key,val):
        self.val = val
        self.key = key
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.tail = ListNode(0,0)
        self.head = ListNode(0,0)
        self.map = {}
        self.capacity = capacity

        self.head.next = self.tail
        self.tail.prev = self.head
        

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        
        node = self.map[key]
        self.remove(node)
        self.add(node)
        return node.val

        

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            old_node = self.map[key]
            self.remove(old_node)
        #add in either condition

        node = ListNode(key,value)
        self.map[key] = node
        self.add(node)
        if len(self.map) > self.capacity:

            to_remove = self.head.next 
            self.remove(to_remove)
            del self.map[to_remove.key]
    def add(self,node):
        prev_end = self.tail.prev
        prev_end.next = node

        node.prev = prev_end
        node.next = self.tail

        self.tail.prev = node


    def remove(self,node):
        node.prev.next = node.next
        node.next.prev = node.prev

