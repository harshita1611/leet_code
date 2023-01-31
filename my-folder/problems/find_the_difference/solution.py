class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        t_set = set(t)
        x=""
        for i in t_set:
            if s.count(i) != t.count(i) :
                x+=i
        return x
