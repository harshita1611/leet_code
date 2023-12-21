class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        x_cords=[]
        for i in points:
            x_cords.append(i[0])
        x_cords.sort()
        max_diff=float("-inf")
        for i in range(len(x_cords)-1):
            gap=x_cords[i+1]-x_cords[i]
            max_diff=max(max_diff,gap)
        
        return max_diff
