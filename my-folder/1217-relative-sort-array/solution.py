class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        ans=[]
        for i in arr2:
            for j in range(len(arr1)):
                if arr1[j]==i:
                    ans.append(arr1[j])
                    arr1[j]=-1
        arr1.sort()

        for i in arr1:
            if i!=-1:
                ans.append(i)
        return ans
