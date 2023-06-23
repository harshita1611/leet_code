class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        mod=10**9 + 7
        n=len(arr)
        def kadane(arr):
            csum=0
            msum=arr[0]
            for i in arr:
                csum+=i
                msum= max(csum , msum)
                if csum<0 :
                    csum = 0 
                if msum<0:
                    msum=0
            return msum
        if k==1:
            return kadane(arr)
        elif sum(arr)<0:
            arr*=2
            return kadane(arr)
        else:
            newarr=arr*2
            return((kadane(newarr)+(sum(arr)*(k-2)))%mod)
        
