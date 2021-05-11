#
# @lc app=leetcode id=1828 lang=python3
#
# [1828] Queries on Number of Points Inside a Circle
#

# @lc code=start
import math


class Solution:
    def countPoints(
        self, points: List[List[int]], queries: List[List[int]]
    ) -> List[int]:
        answer = []

        # for each circle
        for circ_x, circ_y, radius in queries:
            num_of_points = 0

            # for each point
            for x, y in points:
                # calculate distance from center of circle to point
                dist = math.sqrt((circ_x - x) ** 2 + (circ_y - y) ** 2)
                # if dist <= radius, point in circle
                if dist <= radius:
                    num_of_points += 1

            answer.append(num_of_points)

        return answer


# @lc code=end
