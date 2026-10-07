# Oct 6, 2026 939
class Solution:
    def minAreaRect(self, points: list[list[int]]) -> int:

        pointset = set()
        min_size = float("inf")

        for x, y in points:
            pointset.add((x, y))

        for x1, y1 in points:
            for x2, y2 in points:
                if x1 == x2 or y1 == y2:
                    continue
                if (x1, y2) in pointset and (x2, y1) in pointset:
                    min_size = min(min_size, abs((x2 - x1) * (y2 - y1)))

        return min_size if min_size != float("inf") else 0
