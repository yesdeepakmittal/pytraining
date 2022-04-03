import pickle

with open('abc.pickle','wb') as fp:
  pickle.dump(classifier,fp)

with open('abc.pickle','rb') as fp:
  clf = pickle.load(fp)

nltk.classify.accuracy(clf,testing_set)
