class Solution :
    def duplicateZeros(self, arr: list[int]) -> None:
        arr1=[]
        for i in arr :
            arr1.append(i)
            if i==0 :
                arr1.append(0)

        arr=arr1[:len(arr)]
        return arr

obj=Solution()
print(obj.duplicateZeros([1,0,2,3,0,4,5,0]))

#leet code submission
# arr1=[]
#         for i in arr :
#             if i==0 :
#                 arr1.append(0)
#             arr1.append(i)
#         for i in range(len(arr)):
#             arr[i]=arr1[i]