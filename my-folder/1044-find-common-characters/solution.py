class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        freq_0=Counter(words[0])
        for i in words:
            curr_freq=Counter(i)
            for j in freq_0:
                freq_0[j]=min(freq_0[j],curr_freq[j])
        
        res=[]
        for i in freq_0:
            for j in range(freq_0[i]):
                res.append(i)
        return res
