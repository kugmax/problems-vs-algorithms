## HTTPRouter using a Trie

- n - number of sub-paths in path
- m - number on symbols in path

### 1. RouteTrieNode

#### Data structure
The main storage is `dict` where key is the sub-path and value is `RouteTrieNode`.

#### Time Complexity
`insert` happens for `O(1)`

#### Space Complexity 
Each `RouteTrieNode` has 2 references and `children` property has also 2 references per one element: `O(4n)`

### 2. RouteTrie

#### Time Complexity
`insert` and `find` have `O(n)` because needs to traverse all parent sub-paths 

#### Space Complexity
- `insert`: `O(n)` 
- `find` have `O(1)` because there is no there is no dependency between additional space and n

### 3. Router

#### Time Complexity
- `split_path` has `O(m)` 
- `add_handler` has `O(split_path) + O(RouteTrie.insert)` => `O(m + n)`
- `lookup` has `O(split_path) + O(RouteTrie.find)` => `O(m + n)`

#### Space Complexity
- `split_path` has `O(m)`, cause needs to store each sub-path separately
- `add_handler` has `O(split_path) + O(RouteTrie.insert)` => `O(m + n)`
- `lookup` has `O(split_path) + O(RouteTrie.find)` => `O(m)`