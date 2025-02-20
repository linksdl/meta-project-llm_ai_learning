# @lcpr-before-debug-begin
from python3problem29 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=29 lang=python3
# @lcpr version=30204
#
# [29] 两数相除
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1

        # 考虑被除数为最小值的情况
        if dividend == INT_MIN:
            if divisor == 1:
                return INT_MIN
            if divisor == -1:
                return INT_MAX
        
        # 考虑除数为最小值的情况
        if divisor == INT_MIN:
            return 1 if dividend == INT_MIN else 0
        # 考虑被除数为 0 的情况
        if dividend == 0:
            return 0
        
        # 一般情况，使用类二分查找
        # 将所有的正数取相反数，这样就只需要考虑一种情况
        rev = False
        if dividend > 0:
            dividend = -dividend
            rev = not rev
        if divisor > 0:
            divisor = -divisor
            rev = not rev
        
        candidates = [divisor]
        # 注意溢出
        while candidates[-1] >= dividend - candidates[-1]:
            candidates.append(candidates[-1] + candidates[-1])
        
        ans = 0
        for i in range(len(candidates) - 1, -1, -1):
            if candidates[i] >= dividend:
                ans += (1 << i)
                dividend -= candidates[i]

        return -ans if rev else ans
        
# @lc code=end



#
# @lcpr case=start
# 10\n3\n
# @lcpr case=end

# @lcpr case=start
# 7\n-3\n
# @lcpr case=end

# @lcpr case=start
# 0\n1\n
# @lcpr case=end

# @lcpr case=start
# 1\n2\n
# @lcpr case=end

#


