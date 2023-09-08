class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        s = list(s)
        i=0
        while i < len(s) :
            if "".join(s)==goal :
                return True
            s.append(s[0])
            s.pop(0)

            i+=1
            
        return False