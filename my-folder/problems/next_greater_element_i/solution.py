class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack=[]
        res=[-1]*len(nums2)
        for i in range(len(nums2)):
            while stack and nums2[i]>nums2[stack[-1]]:
                index=stack.pop()
                res[index]=nums2[i]
            stack.append(i)

        ans=[]
        for i in range(len(nums1)):
            index_ki_value_num2_mein=nums2.index(nums1[i])
            ans.append(res[index_ki_value_num2_mein])

        return ans