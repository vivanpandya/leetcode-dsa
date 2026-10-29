class Solution:
    def numberOfSubarrays(self, nums, k):
        def atMost(k):
            left = 0
            odd_count = 0
            count = 0

            for right in range(len(nums)):
                if nums[right] % 2 == 1:
                    odd_count += 1

                while odd_count > k:
                    if nums[left] % 2 == 1:
                        odd_count -= 1
                    left += 1

                count += right - left + 1

            return count

        return atMost(k) - atMost(k - 1)

        