class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive_arr=[]
        negative_arr=[]
        for i in nums :
            if i > 0 :
                positive_arr.append(i)
            else :
                negative_arr.append(i)
        n= len(positive_arr)
        arr=[]
        for i in range(n) :
            arr.append(positive_arr[i])
            arr.append(negative_arr[i])
        return arr
