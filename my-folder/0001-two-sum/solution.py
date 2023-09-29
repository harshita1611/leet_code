class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap={}
        for i in range(len(nums)):
            curr = target - nums[i]
            if curr in hashmap.keys() :
                return [hashmap[curr],i]
            else:
                hashmap[nums[i]]=i
