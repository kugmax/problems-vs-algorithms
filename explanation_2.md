## Search in a Rotated Sorted Array
The algorithm is binary search with more sophisticated predicate: 
- because whole array is rotated in one point, one of sub-array must be sorted
- in sorted sub-array checks if target in this sub-array 

### Time complexity
`O(log(n))` as usual binary search. All operation in `is_in_left` predicate happens for `O(1)`.

### Space complexity
`O(1)`, there is no dependency between amount of elements and spaces needed to search target 
