class Solution(object):
    def containsDuplicate(self, nums):
        arr = set(nums)
        if len(arr) != len(nums):
            return True
        
        return False