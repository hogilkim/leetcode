class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        wd = {word[::-1]:i for i,word in enumerate(words)}
        res = []
        
        # for loop through words list
        for idx, word in enumerate(words):
            # for loop through each word
            for i in range(len(word) + 1):
                # make prefix, postfix
                prefix, postfix = word[:i], word[i:]
                # prefix + postfix (this should be palind) + prefix.reverse
                if prefix in wd and idx!=wd[prefix] and postfix==postfix[::-1]:
                    res.append( [ idx, wd[prefix] ] )
                # postfix + prefix + postfix.reverse
                if i>0 and postfix in wd and idx!=wd[postfix] and prefix == prefix[::-1]:
                    res.append([wd[postfix],idx])
                
        return res 