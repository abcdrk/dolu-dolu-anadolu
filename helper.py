import nltk
import pickle

from nltk.tokenize import sent_tokenize

sent_detec = nltk.data.load('tokenizers/punkt/turkish.pickle')

f = open("derlem.txt", encoding="utf-16", errors='ignore')
corpus = f.read()
par_list = corpus.split("\n\n")

par_dict = {}

for par in par_list:
    print(par)
    start = par.index(" ")
    num = par[:start]
    key = int(num)
    par_dict[key] = { "paragraph" : par[start+1:], "sentences" : sent_detec.tokenize(par[start+1:])}

print(len(par_dict))
with open('parToSentences.pickle', 'wb') as handle:
    pickle.dump(par_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)
