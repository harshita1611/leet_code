class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        new_list=[]
        for i in nums :
            new_list.append(i*i)
        new_list.sort()
        print(new_list)


obj = Solution()
obj.sortedSquares([-4,-1,0,3,10])