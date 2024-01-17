class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        right=0
        hashmap={}
        length=0
        n=len(s)
        while right<n:
            char=s[right]
            if char in hashmap and hashmap[char] >=left:
                left=hashmap[char]+1
            hashmap[char] = right
            current_length = right - left + 1

            length = max(length, current_length)
            right += 1

        return length