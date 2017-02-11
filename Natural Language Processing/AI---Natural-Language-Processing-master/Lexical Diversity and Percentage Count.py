import nltk


from nltk.book import *

def lexical_diversity(text):
    return (len(text)/len(set(text)))

def percentage(count, total):
    return(100*count/total)

print("The lexical diversity of text 1 is : ", lexical_diversity(text1))


print("The percentage count of 'the' in text 1 is : ", percentage(text1.count("the"), len(text1)), "percent.")
