"""

572.
Easy

Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. 
A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.

Example 1:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
Given tree t:
   4 
  / \
 1   2
Return true, because t has the same structure and node values with a subtree of s.
Example 2:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
    /
   0
Given tree t:
   4
  / \
 1   2
Return false.

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSubtree2(self, s: TreeNode, t: TreeNode) -> bool:
        
        def help(s, t):
            if not s and not t:
                return True

            if not s or not t:
                return False

            if s.val == t.val:
                l = help(s.left, t.left)
                r = help(s.right, t.right)
                return l and r
        if not s:
            return False
        
        return help(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t) 
    
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        """
        
        Pre-order traversal to serialize the tree and then compare. 
        """
        def bfs(node,f,left=True):
            if node:
                f[0] += '#'+str(node.val)
                bfs(node.left,f,True)
                bfs(node.right,f,False)
            else:
                if left:
                    f[0] += 'ln'
                else:
                    f[0] += 'rn'
                    
            
        finger1 = ['']
        finger2 = ['']
        
        bfs(s,finger1)
        bfs(t,finger2)
        print(finger1,finger2)
        return finger2[0] in finger1[0]