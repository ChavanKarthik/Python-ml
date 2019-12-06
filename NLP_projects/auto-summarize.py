from urllib.request import urlopen

from bs4 import BeautifulSoup

article_url = "https://www.nytimes.com/2019/04/19/technology/youtube-paris-misinformation.html?rref=collection" \
              "%2Ftimestopic%2FArtificial%20Intelligence&action=click&contentCollection=timestopics&region=stream" \
              "&module=stream_unit&version=latest&contentPlacement=4&pgtype=collection "


# get the page content
# page = urlopen(article_url).read().decode('utf8', 'ignore')
# remove html tags
# soup = BeautifulSoup(page, "lxml")

# print(soup.find('article').text)

# text = ' '.join(map(lambda p: p.text, soup.find_all('article')))


# simplify all steps together in a single method(Encapsulation)
def get_text_from_webpage(url):
    page = urlopen(url).read().decode('utf8')
    soup = BeautifulSoup(page, 'lxml')
    text = ' '.join(map(lambda p: p.text, soup.find_all('article')))
    return text


text2 = get_text_from_webpage(article_url)

from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from string import punctuation

# from autocorrect import spell

# text2 = spell(text2)

sentences = sent_tokenize(text2)

word_sent = word_tokenize(text2.lower())
# prepare a list of stopwords
_stopwords = set(
    stopwords.words('english') + list(punctuation) + ['—', '’', '“', '”', 'new', 'said', 'week', 'content'])

# print(_stopwords)

# remove stopwords from actual text
word_sent = [word for word in word_sent if word not in _stopwords]

from nltk.probability import FreqDist  # frequency distribution table

freq = FreqDist(word_sent)  # returns a dictionary with frequency as value
# print(freq)

from heapq import nlargest

top_10_words = (nlargest(10, freq, key=freq.get))
# print(top_10_words)

from collections import defaultdict

ranking = defaultdict(int)

for i, sent in enumerate(sentences):
    for w in word_tokenize(str(sent.lower())):
        if w in freq:
            ranking[i] += freq[w]

# print(ranking)
sentences_idx = nlargest(2, ranking, key=ranking.get)


# print(sentences_idx)

# print([sentences[j] for j in sorted(sentences_idx)])

def summarize(text, n):
    sentences = sent_tokenize(text)

    assert n <= len(sentences)
    word_sent = word_tokenize(text.lower())
    _stopwords = set(stopwords.words('english') + list(punctuation) + ['—', '’', '“', '”', 'new', 'said', 'week'])

    word_sent = [word for word in word_sent if word not in _stopwords]
    freq = FreqDist(word_sent)

    ranking = defaultdict(int)

    for i, sentences in enumerate(sentences):
        for w in word_tokenize(sentences.lower()):
            if w in freq:
                ranking[i] += freq[w]

    sentences_idx = nlargest(n, ranking, key=ranking.get)
    return [sentences[j] for j in sorted(sentences_idx)]


print(summarize(text2, 5))
