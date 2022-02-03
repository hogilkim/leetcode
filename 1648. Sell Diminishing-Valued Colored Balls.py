# solve again
import heapq
class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        inventory.sort(reverse=True)
        inventory.append(0)
        profit = 0
        width = 1
        for i in range(len(inventory)-1):
            if inventory[i] > inventory[i+1]:
                if width * (inventory[i] - inventory[i+1]) < orders:
                    profit += width * self.sumRange(inventory[i+1]+1, inventory[i])
                    orders -= width * (inventory[i] - inventory[i+1])
                else:
                    whole, remaining = divmod(orders, width)
                    profit += width * self.sumRange(inventory[i]-whole+1, inventory[i])
                    profit += remaining * (inventory[i]-whole)
                    break
            width += 1
        return profit % (10**9 + 7)
                    
        
    def sumRange(self, lo, hi):
        # inclusive lo and hi
        return (hi * (hi+1)) // 2 - (lo * (lo-1)) // 2