class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
            n=len(nums)
            s=set()
            for i in range(n):
                for j in range(i+1,n):
                    hashset=set()
                    for k in range(j+1,n):
                        fourth = target-(nums[i]+nums[j]+nums[k])
                        if fourth in hashset :
                            temp=[nums[i],nums[j],nums[k],fourth]
                            temp.sort()
                            s.add(tuple(temp))
                        
                        hashset.add(nums[k])
            return list(s)
