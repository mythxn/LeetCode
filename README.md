| category     | name                                     | notes                                                                                                                |
| -------------- | ------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------- |
| arr          | product of array except self             | two passes; one in order for prefixes, one in reverse for postfixes while computing products                         |
| arr          | find all numbers disappeared in an array | mark indices[val-1] in list as - // return pos[ind+1] of + nums                                                      |
| arr, 2po     | two sum 2 - input arr is sorter          | two pointer // if sum < target, shift left else right                                                                |
| arr, 2po     | 3sum                                     | sort arr; iterate a, if +1 ==, continue; 2sum on rest (2po)                                                          |
| arr, sort    | merge intervals                          | sort intervals by start time; if i[start] <= i-1[end] - end=max(i[end],i-1[end]) else append // think of number line |
| bp           | single number                            | for num, out ^= num // (a^a=0 // 0^a=a)                                                                              |
| bp, arr      | missing number                           | exp sum - act sum // exp sum calc usin math formula                                                                  |
| dp           | climbing stairs                          | recursion; n = n-1 + n-2 // memoization - save in map, possible paths                                                |
| dp           | range sum query - immutable              | create a running total in const // diff bw runTot[right+1] and runTot[left] is the sum                               |
| dp, arr      | best time to buy and sell stock          | slider prob - two pointer sol // iterate thru arr: l=min(l, i), r=max(profit,maxP)                                   |
| dp, d&c, arr | maximum subarray                         | two pointer // iterate thru arr; if l is -, reset curSum, curSum+=n; maxSub = max(l,curS)                            |
| map, arr     | contains duplicate                       | nums len = set(nums) len? bc set returns list wo duplicates                                                          |
| map, arr     | two sum                                  | one pass sol // map[val:idx]; if val in map; return [map[val], idx]; else map[val] = idx                             |
| map, str     | group anagrams                           | map res; for word: map[char freq]; return map.values                                                                 |
| sort         | valid anagram                            | return sorted(a) == sorted(b)                                                                                        |
| stack        | valid parentheses                        | append openings to stack; if not stack and mathing closing- pop(); return True if not stack                          |
