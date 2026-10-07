# solve again
# Oct 6, 2026 963
class Solution:
    def minAreaFreeRect(self, points: list[list[int]]) -> float:
        from collections import defaultdict

        seen = defaultdict(list)
        minarea = float("inf")

        for i, (x1, y1) in enumerate(points):
            for x2, y2 in points[i + 1 :]:
                cx, cy = (x1 + x2) / 2, (y1 + y2) / 2
                d = (x1 - x2) ** 2 + (y1 - y2) ** 2
                for xx, yy in seen[(cx, cy, d)]:
                    area = sqrt(
                        ((x1 - xx) ** 2 + (y1 - yy) ** 2)
                        * ((x2 - xx) ** 2 + (y2 - yy) ** 2)
                    )
                    minarea = min(area, minarea)
                seen[(cx, cy, d)].append((x1, y1))

        return minarea if minarea != float("inf") else 0
