import nltk
from nltk.tokenize import word_tokenize, sent_tokenize

text = "Mary had a little lamb. Her fleece was white as snow"

# split the paragraph into sentences
sentences = sent_tokenize(text)
# print(sentences)

# split the paragraph|sentences into words
words = word_tokenize(text)
# words = [word_tokenize(str(sentences)) for sentence in sentences]
# print(words)

from nltk.corpus import stopwords
from string import punctuation

# build a set of stopwords (set removes duplicates)
custom_stop_words = set(stopwords.words('english') + list(punctuation))
# print(custom_stop_words)

# removing stopwords
words_without_stopwords = [word for word in words if word not in custom_stop_words]
# print(words_without_stopwords)


from nltk.collocations import *  # co-located words

bi_gram_measures = nltk.collocations.BigramAssocMeasures()
finder = BigramCollocationFinder.from_words(words_without_stopwords)
# print(sorted(finder.ngram_fd.items()))  # bigrams with their frequency

text2 = "Mary closed on closing night when she was in the mood to close."
from nltk.stem.lancaster import LancasterStemmer

st = LancasterStemmer()
stemmed_words = [st.stem(word2) for word2 in word_tokenize(text2)]  # stemming sentence
# print(stemmed_words)

# applying parts of speech tagging
# print(nltk.pos_tag(word_tokenize(text2)))

# for ss in wn.synsets('bass'): # to get the diff meanings of a word
#     print(ss, ss.definition())

from nltk.wsd import lesk  # algorithm to give the contextual meaning of a word

sense1 = lesk(word_tokenize("sing in a lower tone,"
                            "along with the bass"), 'bass')

sense2 = lesk(word_tokenize("it was very tasty,"
                            "i liked the bass"), 'bass')
# print(sense2, sense2.definition())
