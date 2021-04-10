"""

LC-460
Hard

Design and implement a data structure for Least Frequently Used (LFU) cache.
It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reaches its capacity,
it should invalidate the least frequently used item before inserting a new item. For the purpose of this problem,
when there is a tie (i.e., two or more keys that have the same frequency), the least recently used key would be evicted.

Note that the number of times an item is used is the number of calls to the get and put functions for that item
since it was inserted. This number is set to zero when the item is removed.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LFUCache cache = new LFUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.get(3);       // returns 3.
cache.put(4, 4);    // evicts key 1.
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4

################  History  #####################

Number of Attempts:     1
Most Recent Attenpt:    2021.04

Similar Problems:
LC-146

Concepts:
doubly-linked list
hashtable

"""

class ListNode:
    def __init__(self, key=None, value=None, freq=0):
        self.key = key
        self.value = value
        self.freq = freq

        self.prev = None
        self.next = None
    
    def __repr__(self):
        return self.__class__.__name__ + f"(key={self.key}, value={self.value}, freq={self.freq})"

class DoublyLinkedList:
    def __init__(self):
        self.head = ListNode()
        self.tail = ListNode()

        self.head.next = self.tail
        self.tail.prev = self.head
    
    def insert_front(self, node: ListNode):
        node.prev = self.head
        node.next = self.head.next

        self.head.next.prev = node
        self.head.next = node
    
    def remove(self, node):
        '''
        Remove node from the list from any place
        '''
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node

    def move_to_front(self, node):
        '''
        Move a node to the front of the linked list
        '''
        self.remove(node)
        self.insert_front(node)

    def remove_last_node(self):
        '''
        Remove the last node and return the removed node
        '''
        node = self.tail.prev
        self.remove(node)
        return node

    def back(self):
        return self.tail.prev

    def is_empty(self):
        if self.head.next == self.tail:
            return True
        return False


class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.items = {}         # key -> node
        self.freq_list = {}     # freq: -> a linked list of nodes
        self.min_freq = 0

    def __len__(self):
        return len(self.items)

    def get(self, key: int) -> int:
        if key not in self.items:
            return -1
        
        else:
            item = self.items[key]
            self.touch(item)
            return item.value

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key not in self.items:
            if len(self) == self.capacity:

                # remove the least recently used item in the linked list for the min_freq
                removed_item = self.freq_list[self.min_freq].remove_last_node()
                if self.freq_list[self.min_freq].is_empty():
                    _ = self.freq_list.pop(self.min_freq)
                    self.min_freq += 1
                self.items.pop(removed_item.key)

            item = ListNode(key=key, value=value, freq=1)
            self.items[key] = item
            self.insert_item_to_freq_list(item)
            self.min_freq = 1
        
        else:
            item = self.items[key]
            item.value = value
            self.touch(item)
    
    def insert_item_to_freq_list(self, item:ListNode):
        if item.freq not in self.freq_list:
            self.freq_list[item.freq] = DoublyLinkedList()
        self.freq_list[item.freq].insert_front(item)
    
    def touch(self, item:ListNode):
        """
        Increase the freq for the item
        """
        prev_freq = item.freq
        _ = self.freq_list[prev_freq].remove(item)
        if self.freq_list[prev_freq].is_empty() and prev_freq == self.min_freq:
            _ = self.freq_list.pop(prev_freq)
            self.min_freq += 1

        freq = prev_freq + 1
        item.freq = freq
        self.insert_item_to_freq_list(item)
                
            
if __name__ == '__main__':

    cache = LFUCache(2)

    cache.put(1, 1)
    cache.put(2, 2)
    print(cache.get(1))         # returns 1
    cache.put(3, 3)             # evicts key 2
    print(cache.get(2))         # returns -1 (not found)
    print(cache.get(3))         # returns 3.
    cache.put(4, 4)             # evicts key 1.
    print(cache.get(1))         # returns -1 (not found)
    print(cache.get(3))         # returns 3
    print(cache.get(4))         # returns 4