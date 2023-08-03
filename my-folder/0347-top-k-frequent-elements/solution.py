class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for i in nums :
            if i  in count :
                count[i]+=1
            elif i not in count:
                count[i]=1
        zxy=sorted(count,key=lambda x:count[x],reverse=True)

        return zxy[:k]
