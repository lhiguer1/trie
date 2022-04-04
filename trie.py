from collections import defaultdict

class Node:
    def __init__(self, value = None):
        self.children = defaultdict(Node)
        self.value = value
            
class Trie:
    def __init__(self):
        self.root = Node()
            
    def find(self, word):
        node = self.root
        for c in word:
            if c in node.children:
                node = node.children[c]
            else:
                return None
        return node.value 
                
    def insert(self, word):
        node = self.root
        for c in word:
            node = node.children[c]
        node.value = word

    @classmethod        
    def root_from_list(cls, words):
        trie = cls()
        for word in words:
            trie.insert(word)
        return trie

if __name__=="__main__":
    words = ["oath","pea","eat","rain"]
    trie = Trie.root_from_list(words)
    print(f'{trie.root.children=}')

    print(trie.find("ass"))