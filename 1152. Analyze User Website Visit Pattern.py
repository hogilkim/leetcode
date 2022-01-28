import collections, itertools
class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        userdict = defaultdict(list)
        
        
        for user, time, web in sorted(zip(username, timestamp, website), key=lambda x:x[1]):
            userdict[user].append(web)
        
        
        
        counter = Counter()
        
        for user, webs in userdict.items():
            counter.update(set(itertools.combinations(webs,3)))
        
        pattern, count = None, 0
        
        for pat, c in counter.items():
            if c>count:
                pattern = pat
                count = c
            elif c == count and pattern>pat:
                pattern = pat
        
        return pattern