## Autocomplete with Tries

- n - number of words stored to autocomplete
- m - length of word

### TrieNode

#### Data structures
The main storage is `dict` where key is the symbol and value `TrieNode`. 

#### Time complexity
- `insert` has `O(1)` complexity (assuming there are no collision)
- `suffixes` is `O(n * m)` in the worst case need to traverse all symbols m in all suffixes n

#### Space complexity
`TrieNode` has 2 references and `children` property has also 2 references per one element: `O(4m)`

### Trie

#### Time complexity
- `insert`: `O(m)` need to traverse all element in word
- `find`: `O(m)` need to traverse all element in prefix

#### Space complexity
 - `insert`: `O(m)`
 - `find`: `O(1)` there is no dependency between additional space and n or m