from sklearn import svm
import numpy as np

# Datos
X = np.array([[0,0], [1,1], [1,0], [0,1]])
y = [0, 0, 1, 1]

# SVM con kernel RBF
clf = svm.SVC(kernel='rbf')
clf.fit(X, y)

print("Predicción:", clf.predict([[0.8, 0.8]]))
