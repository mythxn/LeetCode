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
                left += 1
            num_of_boats += 1
            right -= 1

        return num_of_boats