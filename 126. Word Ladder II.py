class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordList = set(wordList)
        if endWord not in wordList:
            return []
        # BFS visit
        curr_level = {beginWord}
        parents = collections.defaultdict(list)
        while curr_level:
            wordList -= curr_level
            next_level = set()
            for word in curr_level:
                for i in range(len(word)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        new_word = word[:i] + c + word[i+1:]
                        if new_word in wordList:
                            next_level.add(new_word)
                            parents[new_word].append(word)
            if endWord in next_level:
                break
            curr_level = next_level
        # DFS reconstruction
        res = []
        def dfs(word, path):
            if word == beginWord:
                path.append(word)
                res.append(path[::-1])
            else:
                for p_word in parents[word]:
                    dfs(p_word, path + [word])
        dfs(endWord, [])
        return res
# import collections
# class Solution:
#     def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        
#         res = []
#         queue = collections.deque([[beginWord]])
#         wordSet = set(wordList)
#         visited = set()
        
#         while queue and not res:
            
#             updateSet = set()
#             for _ in range(len(queue)):
#                 curr_list = queue.popleft()
#                 last_word = curr_list[-1]
#                 if last_word == endWord:
#                     res.append(curr_list)
#                 else:
#                     for i in range(len(last_word)):
#                         for c in string.ascii_lowercase:
#                             next_word = last_word[:i] + c + last_word[i+1:]
#                             if next_word in wordSet and next_word not in visited:
#                                 queue.append(curr_list + [next_word])
#                                 updateSet.add(last_word)
#             visited.update(updateSet)
                        
        
#         return res