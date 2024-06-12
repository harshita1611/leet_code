class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        right=len(nums)-1
        left=0
        i=0

        while i<=right:
            if nums[i]==0:
                nums[i],nums[left]=nums[left],nums[i]
                if i==left:
                    i+=1
                left+=1
            elif nums[i]==2:
                nums[i],nums[right]=nums[right],nums[i]
                right-=1
            else:
                i+=1        
