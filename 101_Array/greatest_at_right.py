class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        max_right = arr[len(arr)-1]
        arr[len(arr)-1]=-1
        for i in range(len(arr)-2 , -1 ,-1):
            temp = arr[i]
            arr[i]= max_right
            if(max_right<temp):
                max_right=temp
        return arr


obj = Solution()
print(obj.replaceElements([17,18,5,4,6,1]))