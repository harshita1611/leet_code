class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        res = [-1] * len(nums)
        stack = []

        for i in range(2*len(nums)) :
            index = i % len(nums)

            while stack and nums[stack[-1]]<nums[index]:
                curr_index=stack.pop()
                res[curr_index]=nums[index]
            
            stack.append(index)

        return res
      
