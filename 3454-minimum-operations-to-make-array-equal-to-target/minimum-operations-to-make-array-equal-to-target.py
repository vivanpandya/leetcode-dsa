class Solution:
    def minimumOperations(self, nums, target):
        operations = 0
        positive = 0
        negative = 0

        for i in range(len(nums)):
            diff = target[i] - nums[i]

            current_positive = max(0, diff)
            current_negative = max(0, -diff)

            if current_positive > positive:
                operations += current_positive - positive

            if current_negative > negative:
                operations += current_negative - negative

            positive = current_positive
            negative = current_negative

        return operations