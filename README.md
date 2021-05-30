| Category                   | Name                            | Notes                                                                                                                       |
| :--------------------------- | --------------------------------- | :---------------------------------------------------------------------------------------------------------------------------- |
| Array                      | Two Sum                         | 0(n) - One Pass Solution // Map[val: idx]; Traverse the array - if val in Map; return [Map[val], idx]; else Map[val] = idx  |
| Array                      | Contains Duplicate              | return len(nums) == len(set(nums))                                                                                          |
| Array, Dynamic Programming | Best Time to Buy and Sell Stock | Slider Problem // Two Pointer Solution; Iterature through array - sellP = max(sellP, price); if sellP < buyP - buyP = sellP |
