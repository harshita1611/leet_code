class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        hashmap={0:1}
        count=0
        currentsum=0
        for i in nums :
            currentsum+=i
            remainder=currentsum%k
            if remainder in hashmap : 
                count+=hashmap[remainder]
                hashmap[remainder]+=1
            else :
                hashmap[remainder]=1
        return count
