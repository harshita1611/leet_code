class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        new_list=[]
        for i in nums :
            new_list.append(i*i)
        new_list.sort()
        
        return new_list
