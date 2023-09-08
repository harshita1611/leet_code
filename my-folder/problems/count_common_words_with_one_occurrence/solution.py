class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        freq_1={}
        freq_2={}
        for i in words1 :
            if i not in freq_1 :
                freq_1[i]=1
            else :
                freq_1[i]+=1

        for i in words2 :
            if i not in freq_2 :
                freq_2[i]=1
            else :
                freq_2[i]+=1
        
        count=0
        for i in words1:
            if i in freq_1 and i in freq_2 and freq_1[i]==1 and freq_2[i]==1 :
                count+=1        
        return count