class Solution:
    def minSteps(self, s: str, t: str) -> int:
        freq_s ,freq_t=Counter(s),Counter(t)
        
        ans=0
        for i in freq_s:
            if i not in freq_t:
                ans+=freq_s[i]
            elif freq_t[i] < freq_s[i]:
                ans+=(freq_s[i]-freq_t[i])
        
        return ans
