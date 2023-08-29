class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        freq = {}
        for i in nums:
            if i in freq :
                freq[i] += 1
            else :
                freq[i]=1
        result = []
        for i in freq:
            if freq[i] > (n // 3):
                result.append(i)
        return result
