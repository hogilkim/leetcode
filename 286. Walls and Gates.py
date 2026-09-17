# solve again
# Sep 16, 2026 286-2
class Solution:
    def wallsAndGates(self, rooms: list[list[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        from collections import deque

        queue = deque([])
        DIRS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        ROW = len(rooms)
        COL = len(rooms[0])

        for r in range(ROW):
            for c in range(COL):
                if rooms[r][c] == 0:
                    queue.append((r, c))
        while queue:
            r, c = queue.popleft()
            distance = rooms[r][c]

            for rdir, cdir in DIRS:
                nr, nc = r + rdir, c + cdir
                if 0 <= nr < ROW and 0 <= nc < COL and rooms[nr][nc] == 2147483647:
                    rooms[nr][nc] = distance + 1
                    queue.append((nr, nc))


from collections import deque


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        ROW, COL = len(rooms), len(rooms[0])
        queue = deque([])

        for r in range(ROW):
            for c in range(COL):
                if rooms[r][c] == 0:
                    queue.append((r, c))

        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        while queue:
            x, y = queue.popleft()
            distance = rooms[x][y]

            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy
                if (
                    0 <= new_x < ROW
                    and 0 <= new_y < COL
                    and rooms[new_x][new_y] == 2147483647
                ):
                    rooms[new_x][new_y] = distance + 1
                    queue.append((new_x, new_y))
