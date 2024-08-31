# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word
        self.sorted_word = ''.join(sorted(word))
    def match(self, list_word):
        matches = []
        for candidate in  list_word:
            if len(candidate) == len(self.word) and ''.join(sorted(candidate)) == self.sorted_word:
                matches.append(candidate)
        return matches
