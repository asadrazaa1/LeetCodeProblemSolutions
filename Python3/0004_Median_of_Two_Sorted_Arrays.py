class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        sorted_array = sorted(nums1 + nums2)
        len_sorted_array = len(sorted_array)
        if len_sorted_array % 2 == 0:
            return (sorted_array[len_sorted_array // 2] + sorted_array[(len_sorted_array // 2) - 1]) / 2
        else:
            return sorted_array[len_sorted_array // 2]
