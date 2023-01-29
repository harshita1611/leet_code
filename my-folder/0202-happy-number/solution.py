class Solution:
    def isHappy(self, n: int) -> bool:
        hset=set()
        while n!=1 :
            n = sum([int(i) ** 2 for i in str(n)])

            if n in hset:
                return False
            hset.add(n)

        return True

