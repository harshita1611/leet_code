class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n=len(strs)
        if n==0:
            return ""
        elif n==1:
            return strs[0]
        min_str=min(strs)
        max_str=max(strs)

        
        i=0
        minlen=min(len(min_str),len(max_str))

        while i<minlen and min_str[i]==max_str[i]:
            i+=1
        
        ans=min_str[:i]

        if len(ans)==0:
            return ""
        return ans
