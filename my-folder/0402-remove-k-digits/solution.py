class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack=[]
        for i in num:
            while stack and stack[-1]>i and k>0:
                stack.pop()
                k-=1
            stack.append(i)
        
        while k>0:
            stack.pop()
            k-=1
        
        while len(stack)>0 and stack[0]=='0':
            stack.pop(0)

        
        return "".join(stack) if stack else '0'
