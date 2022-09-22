class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        N = str(n)
        res = sum(len(digits)**i for i in range(1,len(N)))
        
        i = 0
        
        while i < len(N):
            res += sum( digit < N[i] for digit in digits) * (len(digits)**(len(N)-i-1))
            if N[i] not in digits: break
            i+=1
        
        # num exactly same as N: i == len(N)
        return res + (i==len(N))
            