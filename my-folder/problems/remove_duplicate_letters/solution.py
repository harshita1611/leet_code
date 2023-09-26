class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        freq={}
        for i in s:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        stack=[]
        visited_set=set()
        for i in s :
            freq[i]-=1
            if i not in visited_set :
                while stack and stack[-1]>i and freq[stack[-1]] > 0 :
                    visited_set.remove(stack.pop())
                stack.append(i)
                visited_set.add(i)
        return ''.join(stack)