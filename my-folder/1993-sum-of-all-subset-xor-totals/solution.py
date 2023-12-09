class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def find_sum(self,nums,final_xor_sum,index):
            if index==len(nums):
                return final_xor_sum
            sum_include_xor=find_sum(self,nums,final_xor_sum^nums[index],index+1)
            sum_exclude_xor=find_sum(self,nums,final_xor_sum,index+1)

            return  sum_include_xor + sum_exclude_xor

        return find_sum(self,nums,0,0)
