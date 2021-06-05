| category                 | name                                     | notes                                                                                           |
| :----------------------- | ---------------------------------------- | ----------------------------------------------------------------------------------------------- |
| arrays                   | two sum                                  | 0(n) - one pass sol // map[val:idx]; if val in map; return [map[val], idx]; else map[val] = idx |
| arrays                   | contains duplicate                       | nums len = set(nums) len? bc set returns list wo duplicates                                     |
| arrays, bit manipulation | missing number                           | exp sum - act sum // exp sum calc usin math formula                                             |
| arrays                   | find all numbers disappeared in an array | mark indices[val-1] in list as - // return pos[ind+1] of + nums                                 |
| arrays, bit manipulation | single number                            | for num, out ^= num // (a^a=0 // 0^a=a)                                                         |
| sort                     | valid anagram                            | return sorted(a) == sorted(b)                                                                   |
| stack                    | valid parentheses                        | append openings to stack; if not stack and mathing closing- pop(); return True if not stack     |
| dynamic programming      | climbing stairs                          | recursion; n = n-1 + n-2 // memoization - save in map, possible paths                           |
| dynamic programming      | best time to buy and sell stock          | slider prob - two pointer sol // iterate thru arr: l=min(l, i), r=max(profit,maxP)              |
| dynamic programming      | maximum subarray                         | two pointer // iterate thru arr; if l is -, reset curSum, curSum+=n; maxSub = max(l,curS)       |
| dynamic programming      | range sum query - immutable              | create a running total in const // diff bw runTot[right+1] and runTot[left] is the sum          |
