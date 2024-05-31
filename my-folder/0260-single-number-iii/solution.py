class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        n=len(nums)
        freq={}
        for i in range(n):
            if nums[i] in freq:
                freq[nums[i]]+=1
            else:
                freq[nums[i]]=1
        
        # print(freq)
        # print(sorted(freq.items()))
        # print(freq.values())
        ans=[]
        for key,value in freq.items():
            if value==1:
                ans.append(key)
        return ans
