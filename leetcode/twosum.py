class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in dic:
                return [dic[complement], i]
            dic[nums[i]] = i

        return []