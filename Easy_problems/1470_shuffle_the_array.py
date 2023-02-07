class Solution:
    def shuffle(self, nums: list[int], n: int) -> list[int]:
        new_arr=[]
        arr_1=[]
        arr_2=[]
        for i in range(int(len(nums)/2)):
            arr_1.append(nums[i])
        for j in range(int(len(nums)/2) , len(nums)):
            arr_2.append(nums[j])
        for k in range(int(len(nums)/2)):
            new_arr.append(arr_1[k])
            new_arr.append(arr_2[k])
        return new_arr


obj = Solution()
print(obj.shuffle([2,5,1,3,4,7],3))