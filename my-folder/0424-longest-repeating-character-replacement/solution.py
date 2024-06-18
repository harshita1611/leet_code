class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l,r,maxlen,maxfreq,=0,0,0,0
        hashmap=[0]*26
        n=len(s)
        while r<n:
            hashmap[ord(s[r])-ord('A')]+=1
            maxfreq=max(maxfreq,hashmap[ord(s[r])-ord('A')])
            if ((r-l+1)-maxfreq) > k:
                hashmap[ord(s[l])-ord('A')]-=1
                l+=1
            maxlen=max(maxlen,r-l+1)
            r+=1
        return maxlen
