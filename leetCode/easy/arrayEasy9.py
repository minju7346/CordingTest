class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        _dict = {}
        for idx, value in enumerate(nums):
            if value in _dict:
                return [_dict[value], idx]
            _dict[target - value] = idx
