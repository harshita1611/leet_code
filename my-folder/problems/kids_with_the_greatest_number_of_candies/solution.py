class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        arr=[]
        maximum = max(candies)
        for i in candies:
            if i + extraCandies >= maximum:
                arr.append(True)
            else:
                arr.append(False)
        return arr