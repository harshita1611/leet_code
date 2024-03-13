class Solution:
    def pivotInteger(self, n: int) -> int:
        arr=list(range(1,n+1))
        prefix=[0]*n
        suffix=[0]*n

        prefix[0]=arr[0]
        suffix[n-1]=arr[n-1]

        for i in range(1,n):
            prefix[i]=arr[i]+prefix[i-1]

        for i in range(n-2,-1,-1):
            suffix[i]=arr[i]+suffix[i+1]
        
        for i in range(n):
            if prefix[i]==suffix[i]:
                return i+1
        return -1
