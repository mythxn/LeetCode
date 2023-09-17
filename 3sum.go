package leetcode

import "sort"

func threeSum(nums []int) [][]int {
	var res [][]int
	sort.Ints(nums)

	for i := 0; i < len(nums); i++ {
		if i > 0 && nums[i] == nums[i-1] {
			continue
		}
		l, r := i+1, len(nums)-1

		for l < r {
			threeSum := nums[i] + nums[l] + nums[r]

			if threeSum < 0 {
				l++
			} else if threeSum > 0 {
				r--
			} else {
				res = append(res, []int{nums[i], nums[l], nums[r]})
				l++
				for l < r && nums[l] == nums[l-1] {
					l++
				}
			}
		}
	}
	return res
}
