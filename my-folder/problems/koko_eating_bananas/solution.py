class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        while low < high :
            k = (low +high)//2
            rem_hours = 0 
            for i in piles : 
                rem_hours += ceil(i/k)
            if rem_hours <= h :
                high = k
            else :
                low=k+1
        return low