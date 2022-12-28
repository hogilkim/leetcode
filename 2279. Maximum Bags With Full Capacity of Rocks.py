class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        capacity = sorted(capacity[i] - rocks[i] for i in range(len(capacity)))

        bags = 0

        for cap in capacity:
            if additionalRocks >= cap:
                additionalRocks -= cap
                bags += 1
            else: break
        return bags