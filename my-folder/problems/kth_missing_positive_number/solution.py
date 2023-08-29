class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        low = 0
        high = len(arr) - 1
        while low <= high :
          mid = (low+high)//2
          if arr[mid]-(mid + 1) < k : 
            low = mid + 1
          else :
            high = mid-1
        return high+k+1