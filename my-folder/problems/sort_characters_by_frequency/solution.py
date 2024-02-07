class Solution:
    def frequencySort(self, s: str) -> str:
        freq={}
        n=len(s)
        for i in range(n):
            if s[i] in freq:
                freq[s[i]]+=1
            else:
                freq[s[i]]=1
        ans=""
        for i in sorted(freq.items(),key= lambda x:x[1],reverse=True):
            print(i[0],i[1])
            ans+=i[0]*i[1]
        
        return ans
