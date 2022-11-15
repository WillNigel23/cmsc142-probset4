text_file_path = "google-10000-english-no-swears.txt"

valid_words = []
with open(text_file_path) as file:
    for line in file:
        valid_words.append(line.rstrip())

class Node:
    def __init__(self, value):
        self.left_child = None
        self.middle_child = None
        self.right_child = None
        self.value = value
        self.is_end = False

class TernarySearchTree:
    def __init__(self):
        self.root_node = None

    def insert(self, word, node=None):
        """ Inserts the provided word into the ternary search tree.
         - Note: While you can implement this function however you like, we
         think you might have the easiest time writing this funcion recursively.
         To facilitate this, we have included a parameter to indicate the
         current node being compared against.
         - The worst-case runtime of this function should be O(k(n + k)), where
         n is the number of words in the tree and k is the number of characters
         in the word.
         - Note that many string functions will take O(k) time, including any
         splitting or substring operations.
        Parameters
        ------------
        word : str
            The word to be inserted.
        node : Node
            The current node being compared against.
        """

        ### TODO: YOUR CODE HERE ###
        pass

    def contains(self, word, node=None):
        """ Returns True if the provided word is in the ternary search tree
        and False otherwise.
         - Note: While you can implement this function however you like, we
         think you might have the easiest time writing this funcion recursively.
         To facilitate this, we have included a parameter to indicate the
         current node being compared against.
         - The worst-case runtime of this function should be O(k(n + k)), where
         n is the number of words in the tree and k is the number of characters
         in the word.
         - Note that many string functions will take O(k) time, including any
         splitting or substring operations.
        Parameters
        ------------
        word : str
            The word we are searching for.
        node : Node
            The current node being compared against.
        Returns
        ------------
        boolean : True if the word was found. False otherwise.
        """

        ### TODO: YOUR CODE HERE ###
        pass

class Spellchecker:
    def __init__(self, valid_words):
        """ Creates a ternary search tree and stores the provided list of
        valid words in the tree.
        Parameters
        -----------
        valid_words : list[str]
            The list of valid words.
        """

        ### TODO: YOUR CODE HERE ###
        pass

    def getNearbyStrings(self, word):
        """Takes in an input word and returns a list of strings which are an edit
        distance of 1 from the input word. Note that the strings in this list
        will not necessarily be in the valid_words list.
         * Thanks to Peter Norvig for this function! He has a great essay on
         spelling correction here: https://norvig.com/spell-correct.html. *
        Parameters
        -----------
        word : str
            The input word.
        Returns
        -----------
        list[str] : A list of strings which are an edit distance of 1 from the
        input word.
        """
        letters    = 'abcdefghijklmnopqrstuvwxyz'
        splits     = [(word[:i], word[i:])    for i in range(len(word) + 1)]
        deletes    = [L + R[1:]               for L, R in splits if R]
        transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R)>1]
        replaces   = [L + c + R[1:]           for L, R in splits if R for c in letters]
        inserts    = [L + c + R               for L, R in splits for c in letters]
        return list(set(deletes + transposes + replaces + inserts))

    def make_suggestions(self, word):
        """Takes in an input word and searches for words which are an
        edit distance of 1 from the input word in the ternary search tree.
        Returns this list of words.
        Some key points:
         - You can assume that words wil consist only of lowercase alphabetic
         characters. This means you do not need to consider uppercase characters,
         spaces, punctuation, numbers, etc.
         - You should not return any words which are not in the "valid_words" list.
         - You do not need to consider whether the input word is spelled correctly.
         Your function should still return words which are an edit distance of 1
         away from the input word regardless.
        Parameters
        -----------
        word : str
            The input word.
        Returns
        -----------
        list[str] : A list of words from the "valid_words" list which are an edit
        distance of 1 from the input word.
        """

        ### TODO: YOUR CODE HERE ###
        pass

spellchecker = Spellchecker(valid_words)
output = spellchecker.make_suggestions(input())
output.sort()
for word in output:
    print(word)