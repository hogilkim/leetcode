# Oct 10, 2026 792-2
from collections import defaultdict


class Solution:
    def numMatchingSubseq(self, s: str, words: list[str]) -> int:
        hashmap = defaultdict(list)
        for word in words:
            hashmap[word[0]].append(word)

        subseqs = 0

        for char in s:
            remainders = hashmap[char].copy()
            del hashmap[char]

            for word in remainders:
                if len(word) == 1:
                    subseqs += 1
                else:
                    hashmap[word[1]].append(word[1:])

        return subseqs


from collections import defaultdict


class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        word_dict = defaultdict(list)
        count = 0

        for word in words:
            word_dict[word[0]].append(word)

        for char in s:

            temp = word_dict[char]
            word_dict[char] = []

            for subseq in temp:
                if len(subseq) == 1:
                    count += 1
                else:
                    word_dict[subseq[1]].append(subseq[1:])

        return count
