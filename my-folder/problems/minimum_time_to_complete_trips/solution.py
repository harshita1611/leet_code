class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        minimum , maximum = 1 , min(time) *  totalTrips
        while minimum < maximum:
            mid = (minimum + maximum) // 2
            current_time = 0
            for i in range(len(time)):
                current_time = current_time + mid // time[i]
            if current_time >= totalTrips:
                maximum = mid
            else:
                minimum = mid + 1
        return minimum
		