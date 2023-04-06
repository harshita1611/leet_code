class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        position = 1
        count = 1
        while time :
            position += count 
            if position == n:
                count=-1
            if position ==1 :
                count=1
            time-=1
        return position
