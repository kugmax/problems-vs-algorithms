class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = dict()

    def insert(self, char):
        self.children[char] = TrieNode()

    def suffixes(self, suffix=''):
        result = []

        for k in self.children.keys():
            v = self.children[k]

            if v.is_word:
                result.append(suffix + k)

            result.extend(v.suffixes(suffix + k))

        return result


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root

        for char in word:
            if char not in current.children:
                current.insert(char)

            current = current.children[char]

        current.is_word = True

    def find(self, prefix):
        if not prefix:
            return None

        current = self.root

        for char in prefix:
            if char not in current.children:
                return None

            current = current.children[char]
        return current


def assert_equals(expected, actual):
    assert (expected == actual), "expected {0}, actual {1}".format(expected, actual)


if __name__ == "__main__":
    myTrie = Trie()
    wordList = [
        "ant", "anthology", "antagonist", "antonym",
        "fun", "function", "factory",
        "trie", "trigger", "trigonometry", "tripod"
    ]
    for word in wordList:
        myTrie.insert(word)

    assert_equals(
        None,
        myTrie.find("")
    )

    assert_equals(
        ["un", "unction", "actory"],
        myTrie.find("f").suffixes()
    )

    assert_equals(
        ["n", "nction"],
        myTrie.find("fu").suffixes()
    )

    assert_equals(
        ["ction"],
        myTrie.find("fun").suffixes()
    )

    assert_equals(
        ["ger", "onometry"],
        myTrie.find("trig").suffixes()
    )

    assert_equals(
        ["er"],
        myTrie.find("trigg").suffixes()
    )

