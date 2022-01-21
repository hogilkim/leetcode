#solved
#first attempt - Jan 21, 2022
class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        
        id_to_min = {} #key:int , val:set()
        
        for log in logs:
            if log[0] not in id_to_min:
                id_to_min[log[0]] = set()
            id_to_min[log[0]].add(log[1])
        
        
        result =[0]*k
        
        for key in id_to_min.keys():
            uam = len(id_to_min[key])
            
            result[uam-1] += 1
        
        return result