class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        h1={}
        h2={}
        for i in range(len(s)):
            if not h1.get(s[i]):
                h1[s[i]]=t[i]
            if not h2.get(t[i]):
                h2[t[i]]=s[i]
            
            if h1[s[i]]!=t[i] or h2[t[i]]!=s[i]:
                return 0
        return 1
