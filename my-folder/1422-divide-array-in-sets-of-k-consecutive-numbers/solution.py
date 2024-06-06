class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        n=len(nums)
        if n%k != 0:
            return False
        freq={}
        for i in nums:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        
        
        sorted_freq=sorted(freq.keys())
        for i in sorted_freq:
            if freq[i]>0:
                curr=freq[i]
                for j in range(i,i+k):
                    if freq.get(j,0)<curr:
                        return False
                    freq[j]-=curr
        return True
                    
