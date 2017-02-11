from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize

PS = PorterStemmer()

sample_words = ["python", "pythoner", "pythoning", "pythoned", "pythonly"]

for word in sample_words:
    print(PS.stem(word))


new_text = "It is important to by very pythonly while you are pythoning with python. All pythoners have pythoned poorly at least once."

words = word_tokenize(new_text)

print (new_text)

for w in words:
    print(PS.stem(w))
