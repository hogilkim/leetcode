class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        ROW, COL = len(strs), len(strs[0])
        res = 0
        for c in range(COL):
            column = []
            for r in range(ROW):
                column.append(strs[r][c])
            print(column)
            if column != sorted(column):
                res += 1

        return res