class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0: 
            return False 
        primes = [2, 3, 5]
        for i in range(len(primes)): 
            while n % primes[i] == 0: 
                n = n / primes[i]
        return n == 1

