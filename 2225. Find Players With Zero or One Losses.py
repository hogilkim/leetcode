from collections import defaultdict
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        players = set()
        
        res = [[],[]]
        
        lost = defaultdict(int)
        
        for winner, loser in matches:
            players.add(winner); players.add(loser);
            lost[loser]+=1
        
        
        for player in sorted(list(players)):
            if player not in lost:
                res[0].append(player)
            elif lost[player] == 1:
                res[1].append(player)
        
        return res