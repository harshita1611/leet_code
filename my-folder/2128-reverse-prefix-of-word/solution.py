class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        to_rev=0
        n=len(word)
        for i in range(n):
            if word[i]==ch :
                to_rev=i
                break

        return word[to_rev::-1]+word[to_rev+1:]
