'''The program looks for anagrams in a paragraph of text and lists the pairs
of anagrams. Condition: the text must be in one paragraph (no new lines).'''

import collections

anagrams = 0

# Read a paragraph of text:
paragraph = input('Enter a paragraph of text: ')
# Split the paragraph into a list of words:
wordlist = paragraph.split()

# Remove punctuation from the wordlist:
ptn = ('.', ',', ':', ';', '?', '!', '\'', '"', '(', ')', '[', ']', '-', '/', \
       '\\', '+', '*')
for word in wordlist:
    if word.startswith(ptn):
        wordlist[wordlist.index(word)] = word[1:]
for word in wordlist:
    if word.endswith(ptn):
        wordlist[wordlist.index(word)] = word[:-1]

# Find anagrams:
for word in wordlist[1:]:
    for word2 in wordlist[:wordlist.index(word)]:
        if (collections.Counter(word.lower()) \
           == collections.Counter(word2.lower())) and \
           (word.lower() != word2.lower()):
            print('Words "{}" and "{}" are anagrams!'.format(word, word2))
            anagrams += 1
if anagrams == 0:
    print('There are no anagrams in the text.')
