class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        temparr = []
        for i in range(m):
            temparr.append(nums1[i])
        for i in range(n):
            temparr.append(nums2[i])
        temparr.sort()
        nums1.clear()
        nums1.extend(temparr)