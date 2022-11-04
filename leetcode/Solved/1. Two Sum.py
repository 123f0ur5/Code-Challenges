class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}

        for i in range(len(nums)):
            tar = target - nums[i]
            if nums[i] in dic:
                return [dic[nums[i]], i]
            else:
                dic[tar] = i

        # ans = []
        # for i, x in enumerate(nums):
        #     cont = i
        #     for y in nums[i+1:]:
        #         cont += 1
        #         if x+y == target:
        #             ans.append(i)
        #             ans.append(cont)
        #             return ans


solution = Solution()

nums = [2,7,11,15]
target = 9

x = solution.twoSum(nums, target)

print(x)