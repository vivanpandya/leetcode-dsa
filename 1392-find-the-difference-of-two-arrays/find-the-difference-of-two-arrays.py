class Solution:
    def findDifference(self, nums1, nums2):
        set1 = set(nums1)
        set2 = set(nums2)

        answer1 = list(set1 - set2)
        answer2 = list(set2 - set1)

        return (answer1, answer2)
