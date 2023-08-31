class Solution:
    def frequencySort(self, s: str) -> str:
        freq={}
        ans=""
        for i in s :
            if i not in freq :
                freq[i]=1
            else:
                freq[i]+=1
        freq=sorted(freq.items(),key= lambda x:x[1],reverse=True)
        ans+="".join([k*v for k,v in freq])
        return ans
        