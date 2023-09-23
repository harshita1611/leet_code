class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n= len(nums)
        count=0
        currSum = 0 
        freq={}
        for i in range(n) :
            currSum+=nums[i]
            if currSum == k :
                count +=1
            if currSum-k in freq :
                count+= freq[currSum-k]
            if currSum in freq :
                freq[currSum]+=1
            else :
                freq[currSum]=1
        return count
