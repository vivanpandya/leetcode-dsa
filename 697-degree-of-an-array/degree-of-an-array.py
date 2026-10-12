class Solution:
    def findShortestSubArray(self, nums):
        count = {}
        first = {}
        last = {}

        for i, num in enumerate(nums):
            count[num] = count.get(num, 0) + 1

            if num not in first:
                first[num] = i

            last[num] = i
            
        degree = max(count.values())
        shortest = len(nums)

        for num, freq in count.items():
            if freq == degree:
                length = last[num] - first[num] + 1
                shortest = min(shortest, length)

        return shortest




        