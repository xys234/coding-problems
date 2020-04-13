from random import choice
from collections import defaultdict


class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        
        self.items = [] 
        self.ind = defaultdict(set)   # item -> index into the items array
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        
        self.items.append(val)
        self.ind[val].add(len(self.items)-1)
        return len(self.ind[val]) == 1
        
    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        
        # print(self.ind)
        # no value
        if val not in self.ind or not self.ind[val]:
            return False
        else:
            remove_ind = self.ind[val].pop()   # random removal
            if not self.ind[val]:
                self.ind.pop(val)
            
            # set will not add duplicate values. So adding first is OK evenif the last elem is the one to delete
            self.ind[self.items[-1]].add(remove_ind)
            self.ind[self.items[-1]].discard(len(self.items)-1)
            self.items[-1], self.items[remove_ind] = self.items[remove_ind], self.items[-1]
            self.items.pop(-1)
        # print(self.ind)
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        # print(self.ind)
        return choice(self.items)

# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()