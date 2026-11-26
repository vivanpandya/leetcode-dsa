class Solution:
    def merge(self, intervals):
        intervals.sort()

        merged = []

        for start, end in intervals:
            if not merged or merged[-1][1] < start:
                merged.append([start, end])
            else:
                merged[-1][1] = max(merged[-1][1], end)

        return merged