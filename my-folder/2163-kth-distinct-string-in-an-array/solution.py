class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        freq={}
        for i in arr :
            if i not in freq :
                freq[i]=1
            else :
                freq[i]+=1
        arr=[]
        for i in freq :
            if freq[i]==1 :
                arr.append(i)
        if len(arr) < k :
            return ""
        return arr[k-1]
