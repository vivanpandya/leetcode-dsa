class Solution:
    def numOfSubarrays(self, arr):
        even = 1
        odd = 0
        prefix_sum = 0
        count = 0

        for num in arr:
            prefix_sum += num

            if prefix_sum % 2 == 1:
                count += even
                odd += 1
            else:
                count += odd
                even += 1

        return count % (10 ** 9 + 7)