class Solution:
    def minDays(self, bloomDay, m, k):
        if m * k > len(bloomDay):
            return -1

        left = min(bloomDay)
        right = max(bloomDay)

        ans = -1

        while left <= right:
            mid = (left + right) // 2

            bouquets = 0
            count = 0

            for day in bloomDay:
                if day <= mid:
                    count += 1

                    if count == k:
                        bouquets += 1
                        count = 0

                else:
                    count = 0

            if bouquets >= m:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans