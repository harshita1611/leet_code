class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        freq={}
        for i in arr:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        
        sorted_freq=sorted(freq.items(),key=lambda x:x[1])
        for num, count in sorted_freq:
            if count<=k:
                k-=count
                del freq[num]
            else:
                break
        
        return len(freq)