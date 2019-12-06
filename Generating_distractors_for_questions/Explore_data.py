import os

import pandas as pd
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import RegexpTokenizer

file_train_data = os.getcwd() + '/DataSet/sample_train.csv'
file_test_data = os.getcwd() + '/DataSet/sample_test.csv'

train_df = pd.read_csv(file_train_data, low_memory=False)
test_df = pd.read_csv(file_test_data, low_memory=False)

# print(train_df.info())
# print(test_df.info())

# Stop Words are words which do not contain important significance to be used in Search Queries.
stop = stopwords.words('english')
stop = stopwords.words('english')
stop.append("new")
stop.append("like")
stop.append("u")
stop.append("it'")
stop.append("'s")
stop.append("n't")
stop.append('mr.')
stop = set(stop)

train_df['question'] = train_df['question'].str.lower().str.split()
train_df['answer_text'] = train_df['answer_text'].str.lower().str.split()
train_df['distractor'] = train_df['distractor'].str.lower().str.split()
test_df['question'] = test_df['question'].str.lower().str.split()
test_df['answer_text'] = test_df['answer_text'].str.lower().str.split()

tokenizer = RegexpTokenizer(r'\w+')

# Lemmatization for train and test data
train_df['question'] = train_df['question'].apply(
    lambda x: [item.lower() for item in x if item.isalpha() if len(item) > 1 if item not in stop])
train_df['answer_text'] = train_df['answer_text'].apply(
    lambda x: [item.lower() for item in x if item.isalpha() if len(item) > 1 if item not in stop])
train_df['distractor'] = train_df['distractor'].apply(
    lambda x: [item.lower() for item in x if item.isalpha() if len(item) > 1 if item not in stop])
test_df['question'] = test_df['question'].apply(
    lambda x: [item.lower() for item in x if item.isalpha() if len(item) > 1 if item not in stop])
test_df['answer_text'] = test_df['answer_text'].apply(
    lambda x: [item.lower() for item in x if item.isalpha() if len(item) > 1 if item not in stop])

# print(train_df.question)
# print(train_df.answer_text)
# print(train_df.distractor)
# print(train_df.info())
# print(porter.stem('drinking'))


# # train model
# model = Word2Vec(train_df.answer_text, min_count=1)
# # fit a 2d PCA model to the vectors
# X = model[model.wv.vocab]
# pca = PCA(n_components=2)
# result = pca.fit_transform(X)
# # create a scatter plot of the projection
# pyplot.scatter(result[:, 0], result[:, 1])
# words = list(model.wv.vocab)
# for i, word in enumerate(words):
# 	pyplot.annotate(word, xy=(result[i, 0], result[i, 1]))
# pyplot.show()


# from gensim.models import KeyedVectors
# # load the Stanford GloVe model
# filename = 'glove.6B.100d.txt.word2vec'
# model = KeyedVectors.load_word2vec_format(filename, binary=False)
# # calculate: (king - man) + woman = ?
# result = model.most_similar(positive=['woman', 'king'], negative=['man'], topn=3)

# df = pd.read_csv(file_train_data)
# data = []
# for index, row in df.iterrows():
#     data.append((row['question'], row['answer_text'], row['distractor']))
# data_df = pd.DataFrame(data, columns=['question', 'answer_text', 'distractor'])
# print(data_df)
# print(train_df.info())

# get only data to a list from a dataframe
train_data = train_df.values.tolist()
test_data = test_df.values.tolist()
data = train_data + test_data

# Stemming is the process of reducing inflection in words to their root forms such as
# mapping a group of words to the same stem even if the stem itself is not a valid word in the Language.
ps = PorterStemmer()
output_flat_list = []


def stemming(list_to_stem):
    for w in list_to_stem:
        output_flat_list.append(ps.stem(w))


stemming(train_data)
stemming(test_data)


# make nested list to a flat list
def remove_nest(l):
    for i in l:
        if type(i) == list:
            remove_nest(i)
        else:
            output_flat_list.append(i)
        # return output


remove_nest(train_data)

print(len(output_flat_list))
# remove duplicate list elements
output_flat_list = set(output_flat_list)
print(len(output_flat_list), output_flat_list)

# model = Word2Vec(train_data, size=100, window=5, min_count=1, workers=4)
# word_vectors = model.wv
