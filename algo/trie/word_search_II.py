"""

212.
Hard

Given a 2D board and a list of words from the dictionary, find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell, 
where "adjacent" cells are those horizontally or vertically neighboring. 
The same letter cell may not be used more than once in a word.

 

Example:

Input: 
board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
words = ["oath","pea","eat","rain"]

Output: ["eat","oath"]
 

Note:

All inputs are consist of lowercase letters a-z.
The values of words are distinct.


"""

from typing import List

from functools import reduce
from collections import defaultdict


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        # create trie
        Trie = lambda: defaultdict(Trie)
        trie = Trie()
        END = True
        
        for word in words:
            reduce(dict.__getitem__,word,trie)[END] = word
        
        res = set()
        def findstr(i,j,t):
            if END in t:
                res.add(t[END])
                # return
            letter = board[i][j]
            board[i][j] = ""
            if i > 0 and board[i-1][j] in t:
                findstr(i-1,j,t[board[i-1][j]])
            if j>0 and board[i][j-1] in t:
                findstr(i,j-1,t[board[i][j-1]])
            if i < len(board)-1 and board[i+1][j] in t:
                findstr(i+1,j,t[board[i+1][j]])
            if j < len(board[0])-1 and board[i][j+1] in t:
                findstr(i,j+1,t[board[i][j+1]])
            board[i][j] = letter
            
            return 
        
        for i, row in enumerate(board):
            for j, char in enumerate(row):
                if board[i][j] in trie:
                    findstr(i,j,trie[board[i][j]])
        return list(res)


if __name__ == "__main__":
    board = [
    ['o','a','a','n'],
    ['e','t','a','e'],
    ['i','h','k','r'],
    ['i','f','l','v']
    ]
    words = ["oath","pea","eat","rain"]
    
    sol = Solution()
    print(sol.findWords(board, words))