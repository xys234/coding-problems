"""


"""

from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.endofword = False


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        self.words = []

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """

        p = self.root
        for w in word:
            if w not in p.children:
                p.children[w] = TrieNode()
            p = p.children[w]
        p.endofword = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """

        p = self.root
        for w in word:
            if w not in p.children:
                return False
            else:
                p = p.children[w]
        if p.endofword:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """

        p = self.root
        for w in prefix:
            if w not in p.children:
                return False
            else:
                p = p.children[w]
        return True
    
    def suggest_help(self, node, w):
        """
        recursively traverse the trie and return a whole word that matches prefix w
        """
        if node.endofword:
            self.words.append(w)
        
        for c, n in node.children.items():
            self.suggest_help(n, w+c)
    
    def suggest(self, search_word):
        self.words.clear()
        
        p = self.root
        not_matched = False
        prefix = ''
        
        for c in search_word:
            if c not in p.children:
                not_matched = True
                break
            
            p = p.children[c]
            prefix += c
        
        if not_matched:
            return []
        
        self.suggest_help(p, prefix)
        return self.words
            

