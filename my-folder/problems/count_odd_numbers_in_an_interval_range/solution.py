class Solution:
    def countOdds(self, low: int, high: int) -> int:
        count = 0 
        if low%2 !=0 or high%2!=0 :
            count =1
        count +=int((high-low)/2)
        return count