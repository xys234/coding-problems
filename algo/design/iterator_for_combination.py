"""

1286.
Medium


Design an Iterator class, which has:

A constructor that takes a string characters of sorted distinct lowercase English letters and 
a number combinationLength as arguments.
A function next() that returns the next combination of length combinationLength in lexicographical order.
A function hasNext() that returns True if and only if there exists a next combination.
 

Example:

CombinationIterator iterator = new CombinationIterator("abc", 2); // creates the iterator.

iterator.next(); // returns "ab"
iterator.hasNext(); // returns true
iterator.next(); // returns "ac"
iterator.hasNext(); // returns true
iterator.next(); // returns "bc"
iterator.hasNext(); // returns false
 

Constraints:

1 <= combinationLength <= characters.length <= 15
There will be at most 10^4 function calls per test.
It's guaranteed that all calls of the function next are valid.

2019.04.28: How to use generator in recursion

"""

class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.gen = self.combination(characters, combinationLength)
        self.buffer = next(self.gen)

    def next(self) -> str:
        res = self.buffer
        try:
            self.buffer = next(self.gen)
        except StopIteration:
            self.buffer = None
        return res

    def hasNext(self) -> bool:
        return self.buffer is not None

    def combination(self, s, n):
        if n==1:
             for ch in s:
                yield ch
        else:
            for i in range(len(s)-n+1):
                for comb in self.combination(s[i+1:],n-1):
                    yield s[i]+comb 