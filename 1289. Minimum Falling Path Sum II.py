class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        def get_min_two(row):
            min_two = []
            for val, idx in row:
                if len(min_two) < 2:
                    min_two.append((val, idx))
                elif min_two[1][0] > val:
                    min_two.pop()
                    min_two.append((val, idx))
                min_two.sort()
            return min_two
        

        LEN = len(grid)
        first_row = [(val, idx) for idx, val in enumerate(grid[0])]
        dp = get_min_two(first_row)
        for r in range(1, LEN):
            next_dp = []
            for curr_c in range(LEN):
                curr_val = grid[r][curr_c]
                min_val = float('inf')
                for prev_val, prev_c in dp:
                    if curr_c != prev_c:
                        min_val = min(min_val, curr_val + prev_val)
                next_dp.append((min_val, curr_c))
                next_dp = get_min_two(next_dp)
            dp = next_dp
        return min([val for val, _ in dp])