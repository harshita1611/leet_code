class Solution:
    def reverseWords(self, s: str) -> str:
        s1 = s.split()
        ans=""
        for i in range(len(s1)-1 , -1 , -1) :
            ans+=s1[i]
            ans += " "
        
        return ans.strip()