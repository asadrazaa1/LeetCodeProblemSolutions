class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # solution_1
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return i, j
        
        # solution_2
        _dict = {}
        
        for index, val in enumerate(nums):
            if target-val in _dict.keys():
                return _dict[target-val], index
            else:
                _dict[val] = index
                