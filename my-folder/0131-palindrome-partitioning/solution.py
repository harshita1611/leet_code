class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res=[]
        def backtrack(i,curr):
            if i==len(s):
                res.append(curr[:])
            
            for j in range(i,len(s)):
                if s[i:j+1]==s[i:j+1][::-1]:
                    curr.append(s[i:j+1])
                    backtrack(j+1,curr)
                    curr.pop()
        backtrack(0,[])
        return res
