class Solution:
    def minOperations(self, s: str) -> int:
        ans_str_0 = "01"*(len(s)//2)
        ans_str_1 = "10"*(len(s)//2)

        count_0 = 0
        count_1=0
        for i in range(len(s)):
            #010
            if (i%2==0 and s[i]=='0') or (i%2==1 and s[i]=='1'):
                count_0+=1
            if (i%2==0 and s[i]=='1') or (i%2==1 and s[i]=='0'):
                count_1+=1
        return min(count_0,count_1)