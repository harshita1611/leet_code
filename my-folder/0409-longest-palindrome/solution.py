class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq={}
        for i in s:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        
        ans=0
        odd=False
        for i in freq.values():
            if i%2==0:
                ans+=i
            else:
                ans += i-1
                odd=True
        
        if odd:
            ans+=1
        return ans
        
