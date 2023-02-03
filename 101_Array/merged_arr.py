class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        temparr = []
        for i in range(m):
            temparr.append(nums1[i])
        for i in range(n):
            temparr.append(nums2[i])
        temparr.sort()
        nums1.clear()
        nums1.extend(temparr)


obj = Solution()
print(obj.merge([1,2,3,0,0,0], 3 ,[2,5,6],3))
