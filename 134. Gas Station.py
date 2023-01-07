class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        diff = [gas[i]-cost[i] for i in range(len(gas))]

        if sum(diff)<0: return -1

        partsum = 0
        start = 0

        for i in range(len(diff)):
            partsum += diff[i]
            if partsum <0:
                start = i + 1
                partsum = 0
        
        return start

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        diff = [gas[i] - cost[i] for i in range(len(gas))]
        
        
        if sum(diff) < 0: return -1

        part_sum = 0
        start = 0
        for i in range(len(gas)):
            part_sum += diff[i]
            if part_sum < 0:
                part_sum = 0
                start = i + 1
        
        return start
                
        