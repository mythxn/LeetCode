 category                      | name                                                    | notes
 -------------------------------|---------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------
 2po                           | middle of linked list                                   | fast_po = next.next, slow_po = next // return slow_po
 arr                           | product of array except self                            | two passes; one in order for prefixes, one in reverse for postfixes while computing products
 arr                           | find all numbers disappeared in an array                | mark indices[val-1] in list as - // return pos[ind+1] of + nums
 arr                           | valid mountain array                                    | 2 loops // first loop breaks at peak, perform checks; second from peak to end, perform checks
 arr                           | shuffle an array                                        | one liner arr shuffler - random.sample(arr,len(arr))
 arr, 2po                      | container with most water                               | while l < r: mA = max(mA,area); if r > l: shift l else r
 arr, 2po                      | two sum 2 - input arr is sorter                         | if sum < target, shift left else right
 arr, 2po                      | 3sum                                                    | sort arr; iterate a, if +1 ==, continue; 2sum on rest (2po)
 arr, 2po                      | move zeroes                                             | j = 0; if n not 0, nums[j] = n; j+=1; nums[j,end] = 0
 arr, 2po, greedy              | boats to save people                                    | sort arr; left-lowest, right-highest; if sum <= limit: count++; else shift right, count++ (send right alone)
 arr, bin search               | find first and last position of element in sorted array | classic bin search except if n[m] == target, if bias left, shift right until cross left, i will be m when l=r; opposite for right bias
 arr, math                     | partition array into disjoint intervals                 | local_max, global_max; update idx when local_max > nums[i] else global_max = max(global_max, nums[i])
 arr, sort                     | merge intervals                                         | sort intervals by start time; if i[start] <= i-1[end] - end=max(i[end],i-1[end]) else append // think of number line
 bin search                    | first bad version                                       | check if m is bad, yes? shift r, else l; return l
 bp                            | single number                                           | for num, out ^= num // (a^a=0 // 0^a=a)
 bp, arr                       | missing number                                          | exp sum - act sum // exp sum calc using math formula
 dp                            | climbing stairs                                         | recursion; n = n-1 + n-2 // memoization - save in map, possible paths
 dp                            | range sum query - immutable                             | create a running total in const // diff bw runTot[right+1] and runTot[left] is the sum
 dp, arr                       | best time to buy and sell stock                         | slider prob - two pointer sol // iterate thru arr: l=min(l, i), r=max(profit,maxP)
 dp, d&c, arr                  | maximum subarray                                        | iterate thru arr; if l is -, reset curSum, curSum+=n; maxSub = max(l,curS)
 ll                            | remove linked list elements                             | handle if head.val is val; if cur.next = val ? cur.next.next : cur.next
 ll, 2po                       | palindrome linked list                                  | find the middle node,
 map, 2po, ll                  | linked list cycle                                       | fast_po = next.next, slow_po = next // if fast_po == slow_po; return True
 map, 2po, str, sliding window | longest substring without repeating characters          | set; for r in range(len(s)): while r in set: shift l; add r to set
 map, arr                      | contains duplicate                                      | nums len = set(nums) len? bc set returns list wo duplicates
 map, arr                      | two sum                                                 | one pass sol // map[val:idx]; if val in map; return [map[val], idx]; else map[val] = idx
 map, str                      | group anagrams                                          | map res; for word: map[char freq]; return map.values
 sort                          | valid anagram                                           | return sorted(a) == sorted(b)
 stack                         | valid parentheses                                       | append openings to stack; if not stack and matching closing- pop(); return True if not stack
 str, design, greedy           | push dominoes                                           | loop until all dominoes have fallen (step == dominoes); each step does one move of each [standing, left, right] using .replace
 tree, bfs                     | maximum depth of binary tree                            | q = deque(), if root: q.append(root), while q: i = popleft, q.append(kids of i); depth += 1
 tree, recursion               | binary tree pruning                                     | recurse every node, if not child & val = 0; remove by return None
