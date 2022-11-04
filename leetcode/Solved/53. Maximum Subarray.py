class Solution(object):
    def maxSubArray(self, nums):
        max = -2147483646
        new_max = 0
        #cont = 0
        #start = 0
        #end = 0

        for i, x in enumerate(nums):
            new_max += x
            if new_max > max:
                max = new_max
                #end = i
                #cont += 1

            if new_max < 0:
                new_max = 0

            #start = i - cont

        return max#, start, end+1

a = Solution()

nums = [20,10,-50, 1, 2, 3, 50]

x = a.maxSubArray(nums)

print(x[0], nums[x[1]:x[2]])