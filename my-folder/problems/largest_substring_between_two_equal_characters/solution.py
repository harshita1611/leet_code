class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        freq={}
        n=len(s)
        maxSize=-1
        for i in range(n):
            if s[i] not in freq:
                freq[s[i]]=i
            else:
                maxSize=max(maxSize,i-freq[s[i]]-1)
        return maxSize
