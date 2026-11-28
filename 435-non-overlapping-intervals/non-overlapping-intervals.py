class Solution:
    def eraseOverlapIntervals(self, intervals):
        intervals.sort(key = lambda x: x[1])

        count = 0
        prev_end = float('-inf')

        for start, end in intervals:
            if start >= prev_end:
                count += 1
                prev_end = end

        return len(intervals) - count 