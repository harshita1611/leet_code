class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        while len(stones)>1:
            y=stones.pop()
            x=stones.pop()
            if x!=y :
                stones.append(y-x)
                stones.sort()
        if len(stones)!=0:
            return stones[0]
        else:
            return 0 