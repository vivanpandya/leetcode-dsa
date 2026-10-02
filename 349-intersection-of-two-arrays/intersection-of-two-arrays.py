class Solution:
    def intersection(self, nums1, nums2):
        seen = set(nums1)
        result = set()

        for num in nums2:
            if num in seen:
                result.add(num)

        return list(result)
