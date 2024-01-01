class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        count = 0
        g.sort()
        s.sort()
        n=max(len(g),len(s))
        i=0
        j=0
        while i<len(g) and j<len(s):
            if s[j]>= g[i]:
                count+=1
                i+=1
            j+=1
        return count
