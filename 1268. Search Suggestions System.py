# Oct 12, 2026 1268-2
class TrieNode:
    def __init__(self):
        self.children = {}
        self.suggestions = []


class Solution:
    def suggestedProducts(
        self, products: list[str], searchWord: str
    ) -> list[list[str]]:
        root = TrieNode()
        products = sorted(products)
        for prod in products:
            node = root
            for char in prod:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
                node.suggestions.append(prod)

        res = []
        node = root
        nomore = False
        for char in searchWord:
            if char not in node.children:
                nomore = True
            if nomore:
                res.append([])
            else:
                node = node.children[char]
                res.append(node.suggestions[:3])
        return res


class Solution:
    def suggestedProducts(
        self, products: List[str], searchWord: str
    ) -> List[List[str]]:

        products = sorted(products)

        search = ""

        result = []
        starting_index = 0

        for i in range(len(searchWord)):
            search += searchWord[i]
            suggestions = []
            for j in range(starting_index, len(products)):
                if search == products[j][: i + 1]:
                    if not suggestions:
                        starting_index = j
                    suggestions.append(products[j])
                if len(suggestions) == 3:
                    break
            result.append(suggestions.copy())
        return result
