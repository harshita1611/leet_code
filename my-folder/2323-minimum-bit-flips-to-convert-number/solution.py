class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        temp = start ^ goal
        count = 0 
        while temp>0 :
            temp = temp&(temp-1)
            count+=1
        return count
