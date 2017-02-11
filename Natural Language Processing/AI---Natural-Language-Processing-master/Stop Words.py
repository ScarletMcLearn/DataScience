from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


example_sent = "This is a sample sentence, showing off the stop words filtration."

stop_words = set(stopwords.words('english'))

word_tokens = word_tokenize(example_sent)

filtered_sentence = []

for w in word_tokens:
    if w not in stop_words:
        filtered_sentence.append(w)

print("Example Sentence: ", example_sent)

print("Word-Tokenized Text: ", word_tokens)

print("Filtered (of stop words) Sentence: ", filtered_sentence)
