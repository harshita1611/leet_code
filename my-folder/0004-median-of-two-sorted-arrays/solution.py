class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n=len(nums1)
        m=len(nums2)
        nums3=[0]*(n+m)

        i,j,k=0,0,0
        while i<n  and j<m:
            if nums1[i]<nums2[j]:
                nums3[k]=nums1[i]
                i+=1
                k+=1
            else:
                nums3[k]=nums2[j]
                k+=1
                j+=1
        
        while i<n:
            nums3[k]=nums1[i]
            i+=1
            k+=1

        while j<m:
            nums3[k]=nums2[j]
            j+=1
            k+=1
        
        final_len=n+m
        if (final_len)%2==0:
            return float((nums3[final_len//2]+nums3[(final_len//2)-1] )/2   )
        else:
            return float(nums3[final_len//2])
