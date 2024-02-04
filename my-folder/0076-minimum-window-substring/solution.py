class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        t_count = defaultdict(int)
        for char in t:
            t_count[char] += 1

        need_count = len(t_count)
        have_count = 0
        left = 0
        idx_result_window = [0, float('inf')]
        window_count = defaultdict(int)

        for right in range(len(s)):
            char = s[right]
            window_count[char] += 1

            if window_count[char] == t_count[char]:
                have_count += 1

            while have_count == need_count:
                if right - left < idx_result_window[1] - idx_result_window[0]:
                    idx_result_window = [left, right]

                window_count[s[left]] -= 1
                if window_count[s[left]] < t_count[s[left]]:
                    have_count -= 1

                left += 1

        return "" if idx_result_window[1] == float('inf') else s[idx_result_window[0]:idx_result_window[1] + 1]
