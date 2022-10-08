
class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2: return 0
        primes = [True]*n
        primes[0] = primes[1] = False
        
        num_prime = 0
        
        for i in range(2, n):
            if primes[i]:
                num_prime+= 1
                for num in range(2*i, n, i):
                    primes[num] = False
        return num_prime