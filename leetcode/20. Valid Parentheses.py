class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s.count('(') != s.count(')') or s.count('[') != s.count(']') or s.count('{') != s.count('}'):
            return False

        countP = 0
        countB = 0
        countCB = 0
        for x in s:
            if countP < 0 or countB < 0 or countCB < 0:
                return False
            if x == '(' : countP += 1
            if x == ')' : countP -= 1
            if x == '[' : countB += 1
            if x == ']' : countB -= 1
            if x == '{' : countCB += 1
            if x == '}' : countCB -= 1
        
        return True
        
x = Solution()

s = "([)]"

print(x.isValid(s))