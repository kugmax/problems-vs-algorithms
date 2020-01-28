class RouteTrieNode:
    def __init__(self):
        self.handler = None
        self.children = dict()

    def insert(self, sub_path, handler=None):
        self.children[sub_path] = RouteTrieNode()
        self.children[sub_path].handler = handler


class RouteTrie:
    def __init__(self, root_handler):
        self.root = RouteTrieNode()
        self.root.insert("/", root_handler)

    def insert(self, sub_paths, handler):
        current = self.root
        for path in sub_paths:
            if path not in current.children:
                current.insert(path)

            current = current.children[path]

        current.handler = handler

    def find(self, sub_paths):
        if not sub_paths:
            return None

        current = self.root
        for sub_path in sub_paths:
            if sub_path not in current.children:
                return None

            current = current.children[sub_path]
        return current.handler


class Router:
    def __init__(self, root_handler, not_found_handler):
        self.trie = RouteTrie(root_handler)
        self.not_found_handler = not_found_handler

    def add_handler(self, path, handler):
        sub_path = self.split_path(path)
        self.trie.insert(sub_path, handler)

    def lookup(self, path):
        sub_path = self.split_path(path)
        result = self.trie.find(sub_path)

        if result:
            return result

        return self.not_found_handler

    def split_path(self, path):
        if not path:
            return []

        sub_path = ""
        sub_paths = []
        for char in path:
            sub_path += char
            if char != "/":
                continue

            sub_paths.append(sub_path)
            sub_path = ""

        if sub_path:
            sub_paths.append(sub_path)

        return sub_paths


def assert_equals(expected, actual):
    assert (expected == actual), "expected {0}, actual {1}".format(expected, actual)


if __name__ == "__main__":
    router = Router("root handler", "404")
    router.add_handler("/home/about", "about handler")
    router.add_handler("/home/all/", "all handler")
    router.add_handler("/home/all/1", "1 handler")
    router.add_handler("/home/all/1/", "1.1 handler")

    assert_equals("root handler", router.lookup("/"))
    assert_equals("404", router.lookup("wrong"))
    assert_equals("404", router.lookup("/wrong"))
    assert_equals("404", router.lookup("/home"))

    assert_equals("about handler", router.lookup("/home/about"))
    assert_equals("404", router.lookup("/home/about/"))
    assert_equals("404", router.lookup("/home/about/me"))

    assert_equals("404", router.lookup("/home/all"))
    assert_equals("all handler", router.lookup("/home/all/"))
    assert_equals("1 handler", router.lookup("/home/all/1"))
    assert_equals("1.1 handler", router.lookup("/home/all/1/"))
    assert_equals("404", router.lookup("/home/all/2"))
