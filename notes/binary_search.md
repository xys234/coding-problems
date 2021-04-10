# Binary Search Summary

There are two general patterns. Their initializations differ. 


Pattern 1 initializes left and right as `[left, right]`

```python
    
# Pattern 1
l, r = 0, len(A) - 1
while l < r:
    mid = l + (r - l) // 2
    if condition:
        l = mid + 1
    else:
        r = mid
```

Problems using pattern 1:

* [x] LC-162: Find Peak Element

```python

# LC-162
def findPeak(self, A):
    # write your code here
    
    l, r = 0, len(A) - 1
    while l < r:
        mid = l + (r - l) // 2
        if A[mid] < A[mid + 1]:
            l = mid + 1
        else:
            r = mid
    return l


```

* [x] LC-852: Peak Index in a Mountain Array

```python

# LC-852
def peakIndexInMountainArray(self, A):
    l, r = 0, len(A) - 1
    while l < r:
        mid = l + (r - l) // 2
        if A[mid] < A[mid + 1]:
            l = mid + 1
        else:
            r = mid
    return l
```


Pattern 2 initializes left and right as `[left, right)`

```python
    
# Pattern 2
l, r = 0, len(A)
while l < r:
    mid = l + (r - l) // 2
    if condition:
        l = mid + 1
    else:
        r = mid
```

* [x] LC-1351: Count Negative Numbers in a Sorted Matrix

```python

def find_first_negative(self, arr):
    """
    Find the first negative in a non-increasing array
    """
    l, r = 0, len(arr)
    while l < r:
        mid = l + (r - l) // 2
        if arr[mid] >= 0:
            l = mid + 1
        else:
            r = mid
    return l

```

* [x] LC-1283: Find the Smallest Divisor Given a Threshold