class Solution:
    def minSpeedOnTime(self, dist, hour):
        if hour <= len(dist) - 1:
            return -1

        left = 1
        right = 10 ** 7
        ans = -1

        hour_limit = round(hour * 100)

        while left <= right:
            mid = (left + right) // 2

            total_time = 0

            for i in range(len(dist) - 1):
                total_time += (dist[i] + mid - 1) // mid

            remaining = hour_limit - total_time * 100

            if remaining >= 0 and dist[-1] * 100 <= remaining * mid:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans