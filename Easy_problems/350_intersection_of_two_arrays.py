class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        ans=[]
        for i in nums1:
            if i in nums2:
                ans.append(i)
                nums2.remove(i)
        return ans



obj = Solution()
print(obj.intersect([1,2,2,1] , [2]))