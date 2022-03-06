class Solution:
    def climbStairs(self, n):
        return self.counter(n, {})

    def counter(self, stairsRem, savedRes):
        # if crossed last step
        if stairsRem < 0:
            return 0

        # if at last step
        if stairsRem == 0:
            return 1

        # memoization
        if stairsRem in savedRes:
            return savedRes[stairsRem]

        # if at unknown stair
        savedRes[stairsRem] = (
                self.counter(stairsRem - 1, savedRes) +
                self.counter(stairsRem - 2, savedRes))

        return savedRes[stairsRem]