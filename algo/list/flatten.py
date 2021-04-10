class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


def to_string(node):
        
        prev_val, next_val = None, None
        if node.prev:
            prev_val = node.prev.val
        if node.next:
            next_val = node.next.val
        
        return f"Node(val={node.val},prev={prev_val},next={next_val})"

    

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        level = []
        self.walk(head, level)
        
        dummy = Node(0, None, None, None)
        prev = dummy

        for node in level:

            prev.next = node
            node.prev = prev
            prev = node
            
        dummy.next.prev = None
        print([to_string(n) for n in level])
        return dummy.next
        
    
    def walk(self, head, level):
        if not head:
            return None
        
        level.append(head)
        if head.child:
            self.walk(head.child, level)
        self.walk(head.next, level)
        
    
    def deserialize(self, vals):
        head = Node(0, None, None, None)
        prev = head

        for val in vals:
            if val is None:
                continue
            
            new = Node(val, None, None, None)
            prev.next = new
            new.prev = prev
            
            
            prev = new
            
            
        head.next.prev = None
        return head.next


sol = Solution()
sol.flatten(Node(0, None, None, None))