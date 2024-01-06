class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        arr = list(zip(startTime, endTime, profit))
        arr.sort(key=lambda x: x[1])

        def upper_bound(jobs, current_job_index):
            start, end = 0, current_job_index
            while start < end:
                mid = (start + end) // 2
                if jobs[mid][1] <= jobs[current_job_index][0]:
                    start = mid + 1
                else:
                    end = mid
            return start

        dp = [0] * len(arr)
        dp[0] = arr[0][2]

        for i in range(1, len(arr)):
            latest_non_conflicting_job = upper_bound(arr, i) - 1
            pick = arr[i][2] + (dp[latest_non_conflicting_job] if latest_non_conflicting_job >= 0 else 0)
            no_pick = dp[i - 1]
            dp[i] = max(pick, no_pick)

        return dp[-1]

