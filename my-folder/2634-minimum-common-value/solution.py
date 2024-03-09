class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        s=set()
        n=len(nums1)
        m=len(nums2)
        for i in range(n):
            s.add(nums1[i])
        for j in range(m):
            if nums2[j] in s:
                return nums2[j]
        return -1
