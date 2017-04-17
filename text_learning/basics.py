#bag of words
#from sklearn.feature_extraction.text import CountVectorizer
#vectorizer = CountVectorizer()
#create email list
# bag_of_words = vectorizer.fit(email_list)
# bag_of_words = vectorizer.transform(email_list)
# print vectorizer.vocabulary_.get('searchedWorkd')


import nltk
# you ll need to download it for the first time
#nltk.download()
from nltk.corpus import stopwords

sw = stopwords.words("english")
print len(sw)

#stemming with NLTK
#getting the basic part of a word
from nltk.stem.snowball import SnwoballStemmer
stemmer = SnowballStemmer("english")
stemmer.stem("responsivness")