class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # freq={}
        # for i in arr:
        #     if i in freq:
        #         freq[i]+=1
        #     else:
        #         freq[i]=1
        # x=[]
        # for i in freq.values():
        #     if i not in x:
        #         x.append(i)
        #     else:
        #         return False
        # return True
        freq=Counter(arr)
        x=Counter(freq.values())
        for i in freq.values():
            if x[i]!=1:
                return False
        return True
