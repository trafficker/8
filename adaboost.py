from sklearn.model_selection import cross_val_score
from sklearn.datasets import load_iris
from sklearn.ensemble import AdaBoostClassifier
iris = load_iris()
clf = AdaBoostClassifier(n_estimators=100) #迭代100次  
re = cross_val_score(clf,iris.data,iris.target) #分类器的精确度  
re.mean()
print(re)
