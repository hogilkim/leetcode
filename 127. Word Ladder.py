# Dec 23, 2023 127
from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)

        queue = deque([(beginWord, 1)])

        while queue:
            word, steps = queue.popleft()
            for i in range(len(word)):
                for char in "abcdefghijklmnopqrstuvwxyz":
                    new_word = word[:i] + char + word[i+1:]
                    if new_word in wordList:
                        if new_word == endWord: return steps+1
                        queue.append((new_word, steps+1))
                        wordList.remove(new_word)
        
        return 0
