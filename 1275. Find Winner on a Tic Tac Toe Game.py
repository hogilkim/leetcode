class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        ways = [0]*8
        
        player = -1
        for x,y in moves:
            player = player * -1
            
            ways[x] += player
            ways[3+y] += player
            
            
            if x == y:  ways[6]+= player
            if x + y == 2:  ways[7]+= player
            
            if 3 in ways or -3 in ways:
                return "A" if player == 1 else "B"
        
        return "Draw" if len(moves) == 9 else "Pending"
            
            