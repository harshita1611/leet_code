class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low , high = 1 , max(piles)
        while low<high:
            k = (low+high)//2
            hours = sum(ceil(n /k) for n in piles)
            low, high = (low, k) if hours <= h else (k+1, high)
        return low


