class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        dmgsum = sum(damage)
        res = dmgsum
        
        for num in damage:
            if num <= armor:
                res = min(res, dmgsum - num)
            else:
                res = min(res, dmgsum - armor)
            
        
        return res + 1