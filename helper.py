import nltk
import pickle

sent_detector = nltk.data.load('tokenizers/punkt/turkish.pickle')

f = open("derlem.txt", errors='ignore')
corpus = f.read()
par_list = corpus.split("\n")

par_dict = {}

for par in par_list:
    start = par.index(" ")
    num = par[:start]
    key = int(num, 10)
    par_dict[key] = { "paragraph" : par, "sentences" : sent_detector(par)}
    break

print(par_dict)
with open('parToSentences.pickle', 'wb') as handle:
    pickle.dump(par_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)
