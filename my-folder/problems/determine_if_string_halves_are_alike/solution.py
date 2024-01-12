class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n=len(s)
        first=s[:(n//2)]
        second=s[(n//2):]
        
        vowels="aeiouAEIOU"
        count_1=0
        for i in first :
            if i in vowels:
                count_1+=1
        
        count_2=0
        for i in second:
            if i in vowels:
                count_2+=1
        return count_1==count_2