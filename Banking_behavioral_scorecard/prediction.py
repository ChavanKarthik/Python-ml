import os

import numpy as np
import pandas as pd
from imblearn.over_sampling import SMOTE
from sklearn.neighbors import KNeighborsClassifier

train_data_file_path = os.getcwd() + '/data_set/Train.csv'
# shape of train [17522 rows x 2395 columns]
test_data_file_path = os.getcwd() + '/data_set/Test.csv'

train_df = pd.read_csv(train_data_file_path, low_memory=False)
test_df = pd.read_csv(test_data_file_path, low_memory=False)

# print(train_df.head())
# print(test_df.head())

# add the missing column in test df as second column
test_df.insert(1, 'Col2', 999)
# print(train_df.shape)
# print(test_df.shape)

# concat test and train data in one df for feature engg
df = pd.concat([train_df, test_df], axis=0, ignore_index=True, sort=False)

# replace nan values with zeros to avoid calculation error
df.fillna(0)

# Group the similar data into single columns
df['c1'] = df.iloc[:, 0:1]
df['c03_c12'] = df.iloc[:, 2:12].sum(axis=1)
df['c13_c16'] = df.iloc[:, 12:16].sum(axis=1)
df['c17_c28'] = df.iloc[:, 16:28].sum(axis=1)
df['c29_c36'] = df.iloc[:, 28:36].sum(axis=1)
df['c37_c40'] = df.iloc[:, 36:40].sum(axis=1)
df['c41'] = df.iloc[:, 40:41]
df['c42_c43'] = df.iloc[:, 41:43].sum(axis=1)
df['c44_c91'] = df.iloc[:, 43:91].sum(axis=1)
df['c92_c93'] = df.iloc[:, 91:93].sum(axis=1)
df['c94_c105'] = df.iloc[:, 93:105].sum(axis=1)
df['c106_c107'] = df.iloc[:, 105:107].sum(axis=1)
df['c108_c137'] = df.iloc[:, 107:137].sum(axis=1)
df['c138_c140'] = df.iloc[:, 137:140].sum(axis=1)
df['c141_c148'] = df.iloc[:, 140:148].sum(axis=1)
df['c149_c151'] = df.iloc[:, 148:151].sum(axis=1)
df['c152_c159'] = df.iloc[:, 151:159].sum(axis=1)
df['c160_c161'] = df.iloc[:, 159:161].sum(axis=1)
df['c162_c167'] = df.iloc[:, 161:167].sum(axis=1)
df['c168_c170'] = df.iloc[:, 167:170].sum(axis=1)
df['c171'] = df.iloc[:, 170:171]
df['c172_c175'] = df.iloc[:, 171:175].sum(axis=1)
df['c176'] = df.iloc[:, 175:176]
df['c177'] = df.iloc[:, 176:177]
df['c178'] = df.iloc[:, 177:178]
df['c179'] = df.iloc[:, 178:179]
df['c180'] = df.iloc[:, 179:180]
df['c181'] = df.iloc[:, 180:181]
df['c182_c195'] = df.iloc[:, 181:195].sum(axis=1)
df['c196_c198'] = df.iloc[:, 195:198].sum(axis=1)
df['c199'] = df.iloc[:, 198:199]
df['c200_c201'] = df.iloc[:, 199:201].sum(axis=1)
df['c202'] = df.iloc[:, 201:202]
df['c203'] = df.iloc[:, 202:203]
df['c204'] = df.iloc[:, 203:204]
df['c205_c207'] = df.iloc[:, 204:207].sum(axis=1)
df['c208_c212'] = df.iloc[:, 207:212].sum(axis=1)
df['c213'] = df.iloc[:, 212:213]
df['c214_c215'] = df.iloc[:, 213:215].sum(axis=1)
df['c216_c223'] = df.iloc[:, 215:223].sum(axis=1)
df['c224_c225'] = df.iloc[:, 223:225].sum(axis=1)
df['c226_c229'] = df.iloc[:, 225:229].sum(axis=1)
df['c230'] = df.iloc[:, 229:230]
df['c231_c233'] = df.iloc[:, 230:233].sum(axis=1)
df['c234_c291'] = df.iloc[:, 233:291].sum(axis=1)
df['c292_c296'] = df.iloc[:, 291:296].sum(axis=1)
df['c297_c299'] = df.iloc[:, 296:299].sum(axis=1)
df['c300'] = df.iloc[:, 299:300]
df['c301_c303'] = df.iloc[:, 300:303].sum(axis=1)
df['c304'] = df.iloc[:, 303:304]
df['c305_c307'] = df.iloc[:, 304:307].sum(axis=1)
df['c308_c309'] = df.iloc[:, 307:309].sum(axis=1)
df['c310_c377'] = df.iloc[:, 309:377].sum(axis=1)
df['c378'] = df.iloc[:, 377:378]
df['c379'] = df.iloc[:, 378:379]
df['c380_c381'] = df.iloc[:, 379:381].sum(axis=1)
df['c382_c392'] = df.iloc[:, 381:392].sum(axis=1)
df['c393_c395'] = df.iloc[:, 392:395].sum(axis=1)
df['c396'] = df.iloc[:, 395:396]
df['c397_c398'] = df.iloc[:, 396:398].sum(axis=1)
df['c399'] = df.iloc[:, 398:399]
df['c400'] = df.iloc[:, 399:400]
df['c401'] = df.iloc[:, 400:401]
df['c402_c404'] = df.iloc[:, 401:404].sum(axis=1)
df['c405_c422'] = df.iloc[:, 404:422].sum(axis=1)
df['c423_c425'] = df.iloc[:, 422:425].sum(axis=1)
df['c426'] = df.iloc[:, 425:426]
df['c427'] = df.iloc[:, 426:427]
df['c428_c430'] = df.iloc[:, 427:430].sum(axis=1)
df['c431_c488'] = df.iloc[:, 430:488].sum(axis=1)
df['c489_c490'] = df.iloc[:, 488:490].sum(axis=1)
df['c491_c504'] = df.iloc[:, 490:504].sum(axis=1)
df['c505_c506'] = df.iloc[:, 504:506].sum(axis=1)
df['c507_c574'] = df.iloc[:, 506:574].sum(axis=1)
df['c575'] = df.iloc[:, 574:575]
df['c576'] = df.iloc[:, 575:576]
df['c577_c578'] = df.iloc[:, 576:578].sum(axis=1)
df['c579_c584'] = df.iloc[:, 578:584].sum(axis=1)
df['c585_c588'] = df.iloc[:, 584:588].sum(axis=1)
df['c589_c591'] = df.iloc[:, 588:591].sum(axis=1)
df['c592'] = df.iloc[:, 591:592]
df['c593_c594'] = df.iloc[:, 592:594].sum(axis=1)
df['c595'] = df.iloc[:, 594:595]
df['c596'] = df.iloc[:, 595:596]
df['c597'] = df.iloc[:, 596:597]
df['c598_c600'] = df.iloc[:, 597:600].sum(axis=1)
df['c601_c602'] = df.iloc[:, 600:602].sum(axis=1)
df['c603'] = df.iloc[:, 602:603]
df['c604_c605'] = df.iloc[:, 603:605].sum(axis=1)
df['c606'] = df.iloc[:, 605:606]
df['c607'] = df.iloc[:, 606:607]
df['c608_c611'] = df.iloc[:, 607:611].sum(axis=1)
df['c612_c647'] = df.iloc[:, 611:615].sum(axis=1)
df['c616_c647'] = df.iloc[:, 615:647].sum(axis=1)
df['c648_c861'] = df.iloc[:, 647:861].sum(axis=1)
df['c862_c865'] = df.iloc[:, 861:865].sum(axis=1)
df['c866_c877'] = df.iloc[:, 865:877].sum(axis=1)
df['c878'] = df.iloc[:, 877:878]
df['c879_c915'] = df.iloc[:, 878:915].sum(axis=1)
df['c916'] = df.iloc[:, 915:916]
df['c917'] = df.iloc[:, 916:917]
df['c918'] = df.iloc[:, 917:918]
df['c919_c920'] = df.iloc[:, 918:920].sum(axis=1)
df['c921'] = df.iloc[:, 920:921]
df['c922'] = df.iloc[:, 921:922]
df['c923'] = df.iloc[:, 922:923]
df['c924_c925'] = df.iloc[:, 923:925].sum(axis=1)
df['c926'] = df.iloc[:, 925:926]
df['c927'] = df.iloc[:, 926:927]
df['c928'] = df.iloc[:, 927:928]
df['c929_c930'] = df.iloc[:, 928:930].sum(axis=1)
df['c931_c933'] = df.iloc[:, 930:933].sum(axis=1)
df['c934_c2397'] = df.iloc[:, 933:2395].sum(axis=1)
df['c2'] = df.iloc[:, 1:2]
# print(df.shape)


df = df.iloc[:, 2395:]
# print(df.shape)  # (37963, 113)
# print(df.iloc[0:5, -1:])

# train data
training_df = df[df['c2'] != 999]
training_df = training_df.iloc[:, 1:]  # remove c1 column
# print(training_df.columns)

# test data
test_data_df = df[df['c2'] == 999]
test_data_col1 = test_data_df.iloc[:, 0:1]
# print(test_data_col1.head)

test_data_df = test_data_df.iloc[:, 1:-1]  # remove 1st and last columns
# print(test_data_df.columns)


# separate x1, x2, ..xn columns with y1
X = training_df
# X = np.array(X)
X = X.fillna(0)

Y = training_df.iloc[:, -1:]
# Y = Y.astype(np.float64)
# Y = Y.astype(int)

Y = np.array(Y).astype(int)
Y = Y.ravel()
# print(Y['c2'].value_counts())
# print(Y.describe())

smt = SMOTE(random_state=42, ratio=1.0)
X_re_sampled, Y_re_sampled = smt.fit_sample(X, Y)
# check whether re-sampling is done
# print('Mean of Y after re-sampling : ', (Y_re_sampled.mean()))

# # 0.2 test_size means 20% of training data
# X_train, X_test, y_train, y_test = train_test_split(X_re_sampled, Y_re_sampled, test_size=0.2, random_state=2)
# # print(X_train.shape, y_train.shape)
# # print(X_test.shape, y_test.shape)
#
#
# Results = pd.DataFrame({'Model': [], 'F1 Score': []})
#
# # Decision Tree Classifier
# model = DecisionTreeClassifier(max_depth=4)
# model.fit(X_train, y_train)
# y_pred = model.predict(X_test)
#
# res = pd.DataFrame({'Model': ['DecisionTreeClassifier'],
#                     'F1 Score': [f1_score(y_pred, y_test)]})
# Results = Results.append(res)
#
#
# # Random Forest Classifier
# model = RandomForestClassifier(n_estimators=2500, max_depth=4)
# model.fit(X_train, y_train)
# y_pred = model.predict(X_test)
# res = pd.DataFrame({'Model': ['RandomForestClassifier'],
#                     'F1 Score': [f1_score(y_pred, y_test)]})
# Results = Results.append(res)
#
#
# KNeighbors Classifier
model = KNeighborsClassifier()
# model.fit(X_train, y_train)
# y_pred = model.predict(X_test)
# res = pd.DataFrame({'Model': ['KNeighborsClassifier'],
#                     'F1 Score': [f1_score(y_pred, y_test)]})
# Results = Results.append(res)
#
#
# # SVM
# model = SVC(gamma='scale')
# model.fit(X_train, y_train)
# y_pred = model.predict(X_test)
# res = pd.DataFrame({'Model': ['SVC'],
#                     'F1 Score': [f1_score(y_pred, y_test)]})
# Results = Results.append(res)
#
#
# # Logistic Regression
# model = LogisticRegression(solver='lbfgs')
# model.fit(X_train, y_train)
# y_pred = model.predict(X_test)
# res = pd.DataFrame({'Model': ['LogisticRegression'],
#                     'F1 Score': [f1_score(y_pred, y_test)]})
# Results = Results.append(res)
#
#
# # xgboost classifier
# model = XGBClassifier(learning_rate=0.001, n_estimators=2500,
#                       max_depth=4, min_child_weight=0,
#                       gamma=0, subsample=0.7,
#                       colsample_bytree=0.7,
#                       scale_pos_weight=1, seed=27,
#                       reg_alpha=0.00006)
# model.fit(X_train, y_train)
# y_pred = model.predict(X_test)
# res = pd.DataFrame({'Model': ['XGBClassifier'],
#                     'F1 Score': [f1_score(y_pred, y_test)]})
# Results = Results.append(res)

# print(Results)
#                     Model  F1 Score
# DecisionTreeClassifier  0.627803
# RandomForestClassifier  0.709028
# KNeighborsClassifier    0.815512
# SVC                     0.168147
# LogisticRegression      0.625425
# XGBClassifier           0.814540
# Clarifies that KNeighborsClassifier, XGBClassifier works well
#
#

model.fit(X_re_sampled, Y_re_sampled)
y_predictions = model.predict(test_data_df).astype(int).fillna(0)
submission_data = pd.concat([test_data_col1, y_predictions], axis=1)
submission_data.to_csv("submission.csv", index=False)
