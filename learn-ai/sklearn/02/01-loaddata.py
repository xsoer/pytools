from sklearn import datasets

iris = datasets.load_iris()
print(iris.data)

digit = datasets.load_digits()
print("\n", '*digits.data*'*10)
print(digit.data)

print("\n", '*digits.targe*'*10)
print(digit.target)

print("\n", '*digits.image*'*10)
print(digit.images[0])


from sklearn import svm

clf = svm.SVC(gamma=0.001, C=100.)

clf.fit(digit.data[:-1], digit.target[:-1])
clf.predict(digit.data[-1:])
