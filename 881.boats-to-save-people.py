#
# @lc app=leetcode id=881 lang=python3
#
# [881] Boats to Save People
#

# @lc code=start
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        left, right = 0, len(people) - 1
        num_of_boats = 0
        people.sort()

        while left <= right:
            if left == right:
                num_of_boats += 1
                break

            cur_tot = people[left] + people[right]

            if cur_tot <= limit:
                num_of_boats += 1
                left += 1
                right -= 1

            # too heavy, send them alone
            elif cur_tot > limit:
                num_of_boats += 1
                right -= 1

        return num_of_boats


# @lc code=end
