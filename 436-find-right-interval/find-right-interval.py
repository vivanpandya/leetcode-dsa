class Solution:
    def findRightInterval(self, intervals):
        starts = sorted(
            (interval[0], i)
            for i, interval in enumerate(intervals)
        )

        result = []
        
        for start, end in intervals:
            left = 0
            right = len(starts)

            while left < right:
                mid = (left + right) // 2

                if starts[mid][0] >= end:
                    right = mid
                else:
                    left = mid + 1

            if left < len(starts):
                result.append(starts[left][1])
            else:
                result.append(-1)

        return result