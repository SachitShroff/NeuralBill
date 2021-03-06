import nltk

def get_words_in_tweets (tweets):
	all_words = []
	for (words, sentiment) in tweets:
		all_words.extend(words)
	return all_words

def get_word_features(wordlist):
	wordlist = nltk.FreqDist(wordlist)
	word_features = wordlist.keys()
	return word_features

def extract_features(document):
	word_features = get_word_features(document)
	document_words = set(document)
	features = {}
	for word in word_features:
		features['contains(%s)' % word] = (word in document_words)
	return features

def analyze (tweet, classifier):
	if classifier.classify(extract_features(tweet.split())) == "positive":
		return 1
	return -1

def get_classifier (training_set):
	classifier = nltk.NaiveBayesClassifier.train(training_set)
	return classifier
