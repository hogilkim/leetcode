# solve again
# first attempt = Jan 9
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i = j = 0
        res = []
        while i < len(firstList) and j < len(secondList):
            
            curr = [max(firstList[i][0], secondList[j][0]), min(firstList[i][1], secondList[j][1])]
            
            if curr[0] <= curr[1]:
                res.append(curr)
            
            if firstList[i][1] <= secondList[j][1]:
                i+=1
            else:
                j+=1
            
        
        return res