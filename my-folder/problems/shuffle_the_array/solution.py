class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
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