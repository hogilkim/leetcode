class Solution:
    def findNthDigit(self, n: int) -> int:
        # 1-9: 9
        # 10-99: 180 (90*2)
        # 100-999: 270 (900*3)
            
        digit_len = 1
        start = 1
        end = 10
        
        while n > (end-start)*digit_len:
            n -= (end-start)*digit_len
            digit_len += 1
            start *= 10
            end *= 10
        
        num = start + (n-1)//digit_len
        print(f'num: {num}, start: {start}, n: {n}, (n-1)//digit_len: {(n-1)//digit_len}')
        return str(num)[(n-1)%digit_len]