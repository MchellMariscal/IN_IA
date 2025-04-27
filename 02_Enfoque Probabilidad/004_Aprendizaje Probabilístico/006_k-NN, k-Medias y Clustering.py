from sklearn.neighbors import KNeighborsClassifier

X = [[0,0], [1,1], [0,1], [10,10], [10,11], [11,10]]
y = [0, 0, 0, 1, 1, 1]

neigh = KNeighborsClassifier(n_neighbors=3)
neigh.fit(X, y)

print("Predicción:", neigh.predict([[1,0]]))
