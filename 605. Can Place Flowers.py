class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        for idx in range(len(flowerbed)):
            if flowerbed[idx] == 0 and \
            (idx == 0 or flowerbed[idx-1] == 0) and \
            (idx == len(flowerbed)-1 or flowerbed[idx+1] == 0) and \
            n > 0:
                flowerbed[idx] = 1
                n -= 1
            
        
        
        return True if n == 0 else False