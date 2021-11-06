from typing import List, Type


class Trie:
    def __init__(self, value: str, children: List['Trie']) -> None:
        self.value = value
        self.children = children

    def __str__(self) -> str:
        return self.__print_trie()

    def __print_trie(self, indent="", string="") -> str:
        if self is not None:
            string += indent + self.value + "\n"
        if self.children is not None:
            for child in self.children:
                string = child.__print_trie(indent + "   ", string)
        return string

    def add_child(self, child: 'Trie') -> None:
        self.children.append(child)

    def add_children(self, children: List['Trie']) -> None:
        for child in children:
            self.add_child(child)

    def process_word(self, word: str) -> None:
        matching_node = [child for child in self.children if child.value == word[0]]
        # this is the first letter
        if len(matching_node) == 0:
            # add whole word (and add leaf node for previous word)
            branch = self.create_branch(word)
            if len(self.children) == 0:
                self.add_child(Trie('Leaf', []))
            self.add_child(branch)

        else:
            # need to traverse down
            node = matching_node[0]
            if len(word) == 1:
                node.add_child(Trie('Leaf', []))
            else:
                node.process_word(word[1:])

    @staticmethod
    def create_branch(word) -> 'Trie':
        nodes = [Trie(letter, []) for letter in word]
        for i in range(len(nodes) - 1):
            nodes[i].add_child(nodes[i + 1])
        return nodes[0]

    def calculate_typing_help(self, word: str) -> int:
        if word == "!" and len(self.children) > 1:
            return 1
        matching_node = [child for child in self.children if child.value == word[0]]
        if len(matching_node) == 0:
            # the rest is inferred (but need to remove stop at the end)
            return len(word) - 1
        elif len(self.children) > 1:
            # there is a choice to make
            return 1 + matching_node[0].calculate_typing_help(word[1:])
        else:
            # there is no choice
            return matching_node[0].calculate_typing_help(word[1:])

    def calculate_typing(self, word: str) -> int:
        word = word + "!"
        print(word)
        return self.calculate_typing_help(word)


if __name__ == "__main__":
    root = Trie('root', [])
    root.add_child(Trie("dummy", []))
    root.process_word("temp")
    root.process_word("test")
    root.process_word("teething")
    root.process_word("teeth")
    root.process_word("teethings")
    print(root)
    word = "teething"
    print(f"{word}: {root.calculate_typing(word)}")
