class Solution:
    def freq(self,s):
        freq={}
        for i in s :
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        return max(freq.values())-min(freq.values())

    def beautySum(self, s: str) -> int:
        n=len(s)
        ans=0
        for i in range(n):
            for j in range(i+1,n):
                ans+=self.freq(s[i:j+1])
        return ans
