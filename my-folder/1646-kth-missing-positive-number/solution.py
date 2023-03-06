class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        arr1=[]
        for i in range(1,2001):
            if i not in arr:
                arr1.append(i)
        return arr1[k-1]
