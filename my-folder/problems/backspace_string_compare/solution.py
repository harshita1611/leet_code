class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def backspace(x):
            stack=[]
            for i in x:
                if i=="#":
                    if stack:
                        stack.pop()
                else:
                    stack.append(i)
            return stack
        
        s_b=backspace(s)
        t_b=backspace(t)

        return s_b==t_b