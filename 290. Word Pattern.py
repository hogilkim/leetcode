class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pat_to_word = {}
        slist = s.split()

        word_to_pat = {}

        if len(pattern) != len(slist): return False
        for i in range(len(slist)):
            if pattern[i] not in pat_to_word:
                pat_to_word[pattern[i]] = slist[i]
            elif pat_to_word[pattern[i]] != slist[i]:
                return False
            
            if slist[i] not in word_to_pat:
                word_to_pat[slist[i]] = pattern[i]
            elif word_to_pat[slist[i]] != pattern[i]:
                return False
        
        return True