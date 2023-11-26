class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack=[]
        n=len(arr)
        res=[0]*n
        for i in range(n):
            while stack and arr[stack[-1]]>=arr[i]:
                stack.pop()
            if not stack :
                res[i]=arr[i]*(i+1)
            else:
                res[i]=res[stack[-1]]+arr[i]*(i-stack[-1])
            stack.append(i)

        return sum(res)%(10**9+7)