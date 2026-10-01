class Solution:
    def generatePossibleNextMoves(self, currentState: str) -> list[str]:
        if len(currentState) < 2:
            return []
        res = []
        for i in range(len(currentState) - 1):
            if currentState[i] == "+" and currentState[i + 1] == "+":
                copy = list(currentState)
                copy[i] = "-"
                copy[i + 1] = "-"
                res.append("".join(copy))
        return res
