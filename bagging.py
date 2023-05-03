#import numpy as np 
#import pandas as pd 
# pip install -U scikit-learn
import matplotlib.pyplot as plt
import seaborn as sns


#Import scikit-learn dataset library
from sklearn import datasets

#Load dataset
cancer = datasets.load_breast_cancer()


# print the names of the 13 features
print("Features: ", cancer.feature_names)

# print the label type of cancer('malignant' 'benign')
print("Labels: ", cancer.target_names)


from sklearn.model_selection import train_test_split

# Split dataset into training set and test set
X_train, X_test, y_train, y_test = train_test_split(cancer.data, cancer.target, test_size=0.3,random_state=109) # 70% training and 30% test

'''
from sklearn.model_selection import train_test_split
Y = data['Purchased']
X = data.drop(columns=['Purchased'])
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.1, random_state=9)
'''

print('X train shape: ', X_train.shape)
print('Y train shape: ', y_train.shape)
print('X test shape: ', X_test.shape)
print('Y test shape: ', y_test.shape)


# We define the number of trees in the forest in 100. 

from sklearn.ensemble import RandomForestClassifier
#from sklearn.metrics import confusion_matrix

# We define the model
rfcla = RandomForestClassifier(n_estimators=100,random_state=9)

# We train model
rfcla.fit(X_train, y_train)

# We predict target values
Y_predict5 = rfcla.predict(X_test)


# The confusion matrix

from sklearn.metrics import confusion_matrix, accuracy_score
rfcla_cm = confusion_matrix(y_test, Y_predict5)
# Display the Confusion matrix


ac = accuracy_score(y_test, Y_predict5)
print ("Confusion Matrix : \n", rfcla_cm)
print ("Accuracy : ", ac)



f, ax = plt.subplots(figsize=(5,5))
sns.heatmap(rfcla_cm, annot=True, linewidth=0.7, linecolor='black', fmt='g', ax=ax, cmap="BuPu")
plt.title('Random Forest Classification Confusion Matrix')
plt.xlabel('Y predict')
plt.ylabel('Y test')
plt.show()



from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import BaggingClassifier

# Instantiate dt
dt = DecisionTreeClassifier(random_state=1)

# Instantiate bc
bc = BaggingClassifier(base_estimator=dt, n_estimators=50, random_state=1)



from sklearn.metrics import accuracy_score

# Fit bc to the training set
bc.fit(X_train, y_train)

# Predict test set labels
y_pred = bc.predict(X_test)

bgcla_cm = confusion_matrix(y_test, y_pred)
#bgcla_cm
print ("Confusion Matrix : \n", bgcla_cm)

# Evaluate acc_test
acc_test = accuracy_score(y_test, y_pred)
print('Test set accuracy of bc: {:.2f}'.format(acc_test))


from sklearn.ensemble import AdaBoostClassifier

ada_boost_clf = AdaBoostClassifier(n_estimators=30)
ada_boost_clf.fit(X_train, y_train)
y=ada_boost_clf.predict(X_test)

bocla_cm = confusion_matrix(y_test, y)
bocla_cm

print ("Confusion Matrix : \n", bocla_cm)

# Evaluate acc_test
acc_test = accuracy_score(y_test, y_pred)
print('Test set accuracy of bc: {:.2f}'.format(acc_test))
