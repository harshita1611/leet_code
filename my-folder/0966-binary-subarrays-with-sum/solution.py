class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix_sum={0:1}
        current_sum=0
        count=0
        for i in nums:
            current_sum+=i
            if current_sum-goal in prefix_sum :
                count+=prefix_sum[current_sum-goal]
            if current_sum in prefix_sum:
                prefix_sum[current_sum]+=1
            else:
                prefix_sum[current_sum]=1
        return count
