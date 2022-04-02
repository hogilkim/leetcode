import collections, heapq
class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.word_dict = collections.defaultdict(list)
        for idx, word in enumerate(wordsDict):
            self.word_dict[word].append(idx)

    def shortest(self, word1: str, word2: str) -> int:
        min_heap1, min_heap2 = self.word_dict[word1].copy(),self.word_dict[word2].copy()
        heapq.heapify(min_heap1)
        heapq.heapify(min_heap2)
                
        curr1, curr2 = heapq.heappop(min_heap1), heapq.heappop(min_heap2)
        
        min_diff = abs(curr1 - curr2)
        while min_heap1 or min_heap2:
            if min_heap1 and (not min_heap2 or curr1 < curr2):
                curr1 = heapq.heappop(min_heap1)
            elif min_heap2:
                curr2 = heapq.heappop(min_heap2)
            min_diff = min(min_diff, abs(curr1 - curr2))
        
        
        return min_diff


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)