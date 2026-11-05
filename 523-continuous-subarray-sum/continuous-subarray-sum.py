class Solution(object):
    def checkSubarraySum(self, nums, k):
        prefix_sum = 0
        seen = {0: -1}

        for i in range(len(nums)):
            prefix_sum += nums[i]

            if k != 0:
                remainder = prefix_sum % k
            else:
                remainder = prefix_sum

            if remainder in seen:
                if i - seen[remainder] >= 2:
                    return True
            else:
                seen[remainder] = i

        return False
 