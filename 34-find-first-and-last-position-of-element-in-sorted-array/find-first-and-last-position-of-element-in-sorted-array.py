class Solution:
    def searchRange(self, nums, target):
        first = -1
        left = 0
        right = len(nums) - 1

        # First Occurence
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                first = mid
                right = mid - 1

            elif nums[mid] < target:
                left = mid + 1

            else:
                right = mid - 1

        last = -1
        left = 0
        right = len(nums) - 1

        # Last Occurence
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                last = mid
                left = mid + 1

            elif nums[mid] < target:
                left = mid + 1

            else:
                right = mid - 1

        return [first, last]
         