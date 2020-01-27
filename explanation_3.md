## Rearrange Array Elements
Solution has two steps:
- sort array using merge sort
- build result number from sorted array

### Time complexity
Merge sort has `O(n log n)` complexity, plus traversing all elements to build result numbers `O(n)`.
So, complexity is `O(n * log(n) + n )` which is in general `O(n log n)`. (Also there is recursion which 
takes time, but doesn't change whole picture) 

### Space complexity
Merge sort require `O(n)` space, plus `O(n)` space needed to build result numbers. Final space complexity is
`O(2n + extra_variables)` which is still `O(n)`. 
