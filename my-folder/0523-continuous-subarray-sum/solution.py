class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        hashmap={0:-1}
        curr=0
        for i in range(len(nums)):
            curr+=nums[i]
            rem=curr%k
            if rem in hashmap:
                if i-hashmap[rem]>1:
                    return True
            else:
                hashmap[rem]=i
        return False
