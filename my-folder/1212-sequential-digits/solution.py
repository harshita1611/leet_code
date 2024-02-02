class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        nums="123456789"
        ans=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                curr=int(nums[i:j+1])

                if curr > high :
                    break
                if curr >= low:
                    ans.append(curr)
        
        return sorted(ans)
