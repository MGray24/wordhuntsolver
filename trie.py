class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.wordend = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def printtrie(self):
        print("root")
        self.stringrecursivehelper(self.root, 0, "")

    def stringrecursivehelper(self, trie, depth, c):
        if depth != 0:
            if trie.wordend:
                print(f"{' ' * (depth)}{'>'}{c}{'<'}")
            else:
                print(f"{' ' * (depth)}{'>'}{c}")
        for idx, child in enumerate(trie.children):
            if child:
                self.stringrecursivehelper(child, depth+1, chr(idx+ord('a')))

    def insertword(self, word):
        current = self.root
        lowerword = word.lower()
        for let in lowerword:
            idx = ord(let) - ord('a')
            if not current.children[idx]:
                current.children[idx] = TrieNode()
            current = current.children[idx]
        current.wordend = True




t = Trie()
t.insertword("cat")
t.insertword("dog")
t.insertword("cathode")
t.insertword("cabin")
t.insertword("tabin")
t.printtrie()

