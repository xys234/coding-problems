


### Graph

#### Shortest path

Examples:  
1. Unweighted graph: [car-distance](../algo/graph/car_distance.py)
2. Weighted graph: [network-delay-time](../algo/graph/network_delay_time.py)

#### Topological sort
Use depth-first search to do topological sort and cycle detection


Examples:  
1. [course-schedule-I](../algo/graph/course_schedule.py)
2. [course-schedule-II](../algo/graph/course_schedule_II.py)

### Tree 

#### In-order Traversal
In-order traversal produces sorted sequence for a BST. There are two implementations, namely  
*recursive algorithm* and *iterative algorithm*. 

> Recursive Algorithm
```python
inorder_recursive(root, values):
    if root is None:
        return 
    inorder_recursive(root.left, values)
    values.append(root.val)
    in_order.recursive(root.right, values)
```

> Iterative Algorithm
```python
inorder_iterative(root):
    values = []
    stack = []
    curr = root
    while curr or stack:
        if curr:
            stack.append(curr)
            curr = curr.left
        
        elif stack:
            top = stack.pop()
            values.append(val)
            curr = top.right
    return values
```             
#### Pre-order traversal
```python

def bfs(node,f=[''],left=True):
    if node:
        f[0] += '#'+str(node.val)
        bfs(node.left,f,True)
        bfs(node.right,f,False)
    else:
        if left:
            f[0] += 'ln'
        else:
            f[0] += 'rn'

```