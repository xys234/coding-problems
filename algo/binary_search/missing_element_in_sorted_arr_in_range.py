"""



amazon, paypal

Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, 
implement a method to find the one that is missing from the array. 
For example, given nums = [0, 1, 3] return 2.

"""

def find_missing_num(nums):
    
    l, r = 0, len(nums)
    while l < r:
        mid = l + (r - l) // 2
        if nums[mid] == mid:
            l = mid + 1
        else:
            r = mid
    return l


if __name__ == "__main__":
    method = find_missing_num

    cases = [
        (method, ([0,1,2], ), 3),
        (method, ([0,1,3], ), 2),
        (method, ([0,1,2,4], ), 3),
        (method, ([0,2,3,4], ), 1),
        (method, ([1,2,3,4], ), 0),
        (method, ([0,1,2,3], ), 4),
    ]

    for i, (func, case, expected) in enumerate(cases):
        ans = func(*case)
        if ans == expected:
            print("Case {:d} Passed".format(i + 1))
        else:
            print("Case {:d} Failed; Expected {:s} != {:s}".format(i + 1, str(expected), str(ans)))