import math
class Solution:
    def findGCD(self, nums: list[int]) -> int:
        return math.gcd(min(nums) , max(nums))

obj = Solution()
print(obj.findGCD([2,5,6,9,10]))