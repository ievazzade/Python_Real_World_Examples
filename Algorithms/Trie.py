from TrieNode import TrieNode

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def get_index(self, t):
        return ord(t) - ord('a')
    
    def insert(self, key):
        if key is None:
            return False
        
        key = key.lower()
        current = self.root

        for letter in key:
            index = self.get_index(letter)

            if current.children[index] is None:
                current.children[index] = TrieNode(letter)
                print(letter, "inserted!")
            
            current = current.children[index]
        
        current.is_end_word = True
        print("'" + key + "' inserted!")
    
    def search(self, key):
        if key is None:
            return False
        
        key = key.lower()
        current = self.root

        for letter in key:
            index = self.get_index(letter)
            if current.children[index] is None:
                return False
            current = current.children[index]
        
        if current is not None and current.is_end_word:
            return True

        return False

    def delete_helper(self, key, current, length, level):
        deleted_self = False

        if not current:
            print("Key does not exist")
            return deleted_self
        
        if level is length:
            print("Level is length, we are at the end")
            if current.children.count(None) == len(current.children):
                print("- Node", current.char, ": has no children, delete it.")
                current = None
                deleted_self = True
            else:
                print("- Node", current.char, ": has children, don't delete it")
                current.is_end_word = False
                deleted_self = False
        else:
            index = self.get_index(key[level])
            print("Traverse to", key[level])
            child_node = current.children[index]
            child_deleted = self.delete_helper(key, child_node, length, level + 1)
            if child_deleted:
                print("-Delete Link from", current.char, "to", key[level])
                current.children[index] = None
                

    def delete(self, key):
        if not self.root or not key:
            print("None key or empty trie error")
            return
        print("\nDeleting: ", key)
        self.delete_helper(key, self.root, len(key), 0)

if __name__ == "__main__":
    keys = ["the", "a", "there", "answer", "any",
            "by", "bye", "their", "abc"]
    res = ["Not present in trie", "Present in trie"]
    t = Trie()
    print("Keys to insert: \n", keys)

    for words in keys:
        t.insert(words)

    # Search for different keys
    print("the --- " + res[1] if t.search("the") else "the --- " + res[0])
    print("these --- " + res[1] if t.search("these") else "these --- " + res[0])
    print("abc --- " + res[1] if t.search("abc") else "abc --- " + res[0])