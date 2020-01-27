## Dutch National Flag Problem
The problem was solve using three pointers: `pointer_0` shows end of 0-area at the begin, `pointer_2` shows
start of 2-area from end, and `i` shows the current main pointer.  

### Time complexity
`O(n)` since the whole array traverse only once.

### Space complexity
`O(1)` there is no dependencies between array length and additional space needed to traverse it. All modifications happens
at place.
