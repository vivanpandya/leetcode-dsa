class Solution:
    def maxScore(self, cardPoints, k):
        n = len(cardPoints)
        total = sum(cardPoints)

        window_size = n - k

        if window_size == 0:
            return total

        window_sum = sum(cardPoints[:window_size])
        min_sum = window_sum

        for right in range(window_size, n):
            window_sum += cardPoints[right]
            window_sum -= cardPoints[right - window_size]

            min_sum = min(min_sum, window_sum)

        return total - min_sum
