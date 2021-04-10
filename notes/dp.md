# Dynamic Programming Summary


Dynamic programming problems usually solve for optimization problems and count the number of ways. The problem usually asks for longest, shortest, maximum, minimum, or number of ways. 


## 1. Prefix Sub-Problem
The sub-problem is for a prefix sub-array. Usually, the state transition takes the following form

`dp[i] = f{dp[i-k], g(arr[i-k:i])} for k in [i-kmax, i)`

This `g` function should be evaluated easily. and `dp[i-k]` is previously solved since it is a prefix
shorter than dp[i].

* [x] LC-32: Longest Valid Parentheses
* [x] LC-140: Word Break II
* [x] LC-152: Maximum Subarray Product
* [x] LC-343: Integer Break
* [x] LC-639: Decode Ways II
* [x] LC-1027 Longest Arithmetic Sequence
* [x] LC-1411: Number of Ways to Paint N × 3 Grid
* [x] LC-1425: Constrained Subsequence Sum

## 2. Suffix Sub-Problem
The sub-problem is for a suffix sub-array. The state transition is the opposite of the prefix category. 
`g` involves the prefix array of the current suffix sub-array. 

Example problems include
* [x] LC-1402: Reduce Dishes
* [x] LC-1416: Restore Arrays
* [x] LC-1420: Build Array Where You Can Find The Maximum Exactly K Comparisons


## 3. Subarray Sub-Problem
The sub-problem is for a sub-array of the original array



## 4. Two Sequences

For this type of problem, the sub-problem usually takes the form of the first i elements and first j elements of the two sequences, expressed as `dp[i][j]`. The complexity is `O(mn)`. 

The state transition usually considers whether to use the current elements, namely the `i`th and the `j`th element, of both sequences. 

Example problems include 
* [x] LC-10
* [x] LC-44
* [x] LC-72
* [x] LC-97 
* [x] LC-801
* [x] LC-1092
* [x] LC-1143
* [x] LC-1458

## 5. Grid-based DP


## 6. Tree-based DP




## 7. Bit State Representation

States are expressed by a bit mask. 
Example problems include
* [x] LC-1434:  Number of Ways to Wear Different Hats to Each Other




