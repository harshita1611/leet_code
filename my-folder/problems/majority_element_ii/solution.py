class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        dict={}
        for i in range(len(nums)):
            try:
                dict[nums[i]]+=1
            except:
                dict[nums[i]]=1
        key=list(dict.keys())
        value=list(dict.values())
        res=[]
        for i in range(len(value)):
            if value[i]>len(nums)//3:
                res.append(key[i])
        return res