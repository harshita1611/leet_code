class Solution:
    def maxScore(self, s: str) -> int:
        max_score=0
        for i in range(1,len(s)):
            left=s[:i]
            right=s[i:]
            left_count=left.count('0')
            right_count=right.count('1')

            if (left_count + right_count)> max_score:
                max_score= left_count + right_count

        return max_score