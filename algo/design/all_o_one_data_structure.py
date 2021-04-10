"""

432.
Hard

"""

class Node:
    def __init__(self, value):
        self.value = value
        self.items = set()
        self.prev = None
        self.next = None
    
    def __len__(self):
        return len(self.items)
        
    def add(self, item : str):
        """
        Add string items
        """
        self.items.add(item)
    
    def remove(self, item : str):
        self.items.remove(item)
    
    def insert_right(self, new_node):
        """
        Insert the `new_node` between this node and next
        """
        
        old_next = self.next
        self.next = new_node
        new_node.prev = self
        new_node.next = old_next
        old_next.prev = new_node
    
    def insert_left(self, new_node):
        
        old_prev = self.prev
        self.prev = new_node
        new_node.next = self
        new_node.prev = old_prev
        old_prev.next = new_node
    
    def delete(self):
        """
        delete the current node
        """
        
        curr_prev = self.prev
        curr_next = self.next
        
        curr_prev.next = curr_next
        curr_next.prev = curr_prev

        
class AllOne:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        
        self.d = {}
        self.head = Node(0)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def is_empty(self):
        if self.head.next.value == -1:
            return True
        return False

    def inc(self, key: str) -> None:
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        """
        if key not in self.d:
            
            # value 1 exists but this key is not present
            if self.head.next.value == 1:
                self.head.next.add(key)
            else:
                node = Node(1)
                node.add(key)
                self.head.insert_right(node)
        else:
            node = self.d[key]
            if node.next.value != node.value + 1:
                new = Node(node.value + 1)
                new.add(key)
                node.insert_right(new)
            else:
                node.remove(key)
                node.next.add(key)
            

    def dec(self, key: str) -> None:
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        """
        
        if key in self.d:
            
            node = self.d[key]
            node.remove(key)
            
            if node.value == 1:
                self.d.remove(key)
            else:
                if node.prev.value == node.value - 1:
                    node.prev.add(key)
                else:
                    new_node = Node(node.value - 1)
                    node.insert_left(new_node)
            
            if len(node) == 0:
                node.delete()
        

    def getMaxKey(self) -> str:
        """
        Returns one of the keys with maximal value.
        """
        if not self.is_empty():
            return next(iter(self.tail.prev.items))
        return ""
        

    def getMinKey(self) -> str:
        """
        Returns one of the keys with Minimal value.
        """
        
        if not self.is_empty():
            return next(iter(self.head.next.items))
        return ""