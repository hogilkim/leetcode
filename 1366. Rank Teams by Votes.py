# Feb 1, 2024 1366-2
class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        ranks = {char:[0]*len(votes[0]) for char in votes[0]}

        for vote in votes:
            for idx, char in enumerate(vote):
                ranks[char][idx] -= 1
        
        res = sorted([key for key in ranks.keys()])
        res = sorted(res, key=lambda x:ranks[x])
        return "".join(res)


class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        votedict = {char:[0]*len(votes[0]) for char in votes[0]}
        
        for vote in votes:
            for idx, char in enumerate(vote):
                votedict[char][idx]+=1
        
        vote_result = sorted([(key, val) for key, val in votedict.items()], key=lambda x:x[0])
        vote_result = sorted(vote_result, key=lambda x:x[1], reverse=True)
        # print(vote_result)
        return "".join([key for key, val in vote_result])