class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = {}
        n = len(s)
        for i in range(n):
            if s[i] in freq:
                freq[s[i]] += 1
            else:
                freq[s[i]] = 1
        for i in range(n):
            if freq[s[i]] == 1:
                return i
        return -1