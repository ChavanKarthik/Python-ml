from sklearn import tree

# [height, weight, shoe size, running speed km/hr]
X = [[180, 75, 44, 35], [177, 70, 43, 34], [181, 80, 44, 36], [160, 60, 38, 30], [162, 61, 38, 28], [161, 59, 37, 29]]
Y = ['male', 'male', 'male', 'Female', 'Female', 'Female']

clf = tree.DecisionTreeClassifier()

clf = clf.fit(X, Y)

prediction = clf.predict([[171, 66, 39, 35]])

print(prediction)
