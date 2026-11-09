class Solution:
    def minSubarray(self, nums, p):
        total = sum(nums)
        target = total % p

        if target == 0:
            return 0

        prefix = 0
        min_length = len(nums)
        last_seen = {0: -1}

        for i in range(len(nums)):
            prefix = (prefix + nums[i]) % p

            needed = (prefix - target) % p

            if needed in last_seen:
                min_length = min(min_length, i - last_seen[needed])

            last_seen[prefix] = i

        if min_length == len(nums):
            return -1

        return min_length