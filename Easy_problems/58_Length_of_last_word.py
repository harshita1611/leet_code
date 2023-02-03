class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count=0
        s=s.strip()
        split = s.split(" ")
        return len(split[-1])


obj = Solution()
print(obj.lengthOfLastWord("   fly me   to   the moon  "))