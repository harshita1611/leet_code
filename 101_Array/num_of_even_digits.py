class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        count=0
        for i in nums :
            number = str(i)
            digits = len(number)
            if digits%2==0 :
                count+=1
        print(count)
obj = Solution()
obj.findNumbers([12,345,2,6,7896])