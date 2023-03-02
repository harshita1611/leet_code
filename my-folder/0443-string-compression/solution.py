
class Solution:
    def compress(self, chars: List[str]) -> int:
        idx = 0
        index = 0
        while idx < len(chars):
            chars[index] = chars[idx]
            k = idx
            while idx < len(chars) and chars[idx] == chars[k]:
                idx += 1

            n = idx - k
            index += 1
            if n > 1:
                for c in str(n):
                    chars[index] = c
                    index += 1
        return index
