# Heap Summary

## Idea

1. provides a way to process the elements in an array in a sorted sequence. 
2. It is also usually used for find the top k elements in an array. 

## Examples

* [x] LC-973: K-closest points to origin

Solution:
Maintain a max heap of size k. push the element. If the heap already has k elements, then pop the largest element. 

The heap has the k points with the smallest distance. 

```python

def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        h = []
        for x, y in points:
            d = x ** 2 + y ** 2
            if len(h) < K:
                heapq.heappush(h, (-d, [x, y]))
            else:
                heapq.heappushpop(h, (-d, [x, y]))
        
        res = [p[1] for p in h]
        return res

```

* [x] LC-703: Kth Largest Element in a Stream
* [x] LC-215: Kth Largest Element in an Array

Maintain a **min heap** of size k. Push every element in the stream into the heap. 
If the element > the min element, pop the min element. 
The min element is the kth largest since all the other elements are larger. 

* [x] LC-295: Find Median from Data Stream
Maintain two heaps. One for each half. Then the median is always found by the min element and largest element.  

* [x] LC-373: Find K Pairs with Smallest Sums
* [x] LC-378: Kth Smallest Element in a Sorted Matrix
* [x] LC-1439: Find the Kth Smallest Sum of a Matrix With Sorted Rows

Maintain a min heap. Find the next possible smallest sum based on the top element in the heap.