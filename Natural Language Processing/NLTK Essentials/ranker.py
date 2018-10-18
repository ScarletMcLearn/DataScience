import pickle

pos = pickle.load(open('pos_word_list.pkl', 'rb'))

neg = pickle.load(open('neg_word_list.pkl', 'rb'))

pos_dict = []
neg_dict = []


print("Starting with Positives. ")
print()

for _ in range(3):
    print("Word #", str(_), ": ", pos_dict[_])
    