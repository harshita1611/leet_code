class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count=0
        s=s.strip()
        split = s.split(" ")
        return len(split[-1])


