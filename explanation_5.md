## Autocomplete with Tries

- w - number of words stored to autocomplete
- m - number of symbols in the word
- n - number of elements in function argument

### TrieNode

#### Data structures
The main storage is `dict` where key is the symbol and value `TrieNode`. 

#### Time complexity
- `insert` has `O(1)` complexity (assuming there are no collision)
- `suffixes` is `O(m * w)` # TODO:  !!!!!!

#### Space complexity
`TrieNode` has 2 references where `children` property has also 2 references per one element: `O(4m)` #TODO: !!!

### Trie

#### Time complexity
- `insert`: `O(n)` need to traverse all element in word
- `find`: `O(n)` need to traverse all element in prefix

#### Space complexity
 - `insert`: `O(n)`
 - `find`: `O(1)` there is no dependency between additional space and n, m or w  #TODO: !!!!