# -*- coding: utf-8 -*-
"""
Created on Tue Oct 21 19:50:54 2014

@author: Karim
"""

import pandas as pd
import numpy as np
from patsy import dmatrices
import statsmodels.api as sm 


from sklearn.ensemble import RandomForestClassifier

test_path = "test.csv"
train_path = "train.csv"

train_df = pd.read_csv(train_path)
test_df = pd.read_csv(test_path)

mean_age = np.mean(train_df.Age)
train_df.Age = train_df.Age.fillna(mean_age)

test_df.Age = test_df.Age.fillna(mean_age)
test_df["Survived"] = 0
test_passengers = test_df.PassengerId.values

formula_ml = "Survived ~ C(Pclass) + C(Sex) + Age + SibSp + Parch + C(Embarked)"
#formula_ml = "Survived ~ C(Sex)"

results = {}


train_y, train_x = dmatrices(formula_ml, data=train_df, return_type="dataframe")
test_y, test_x = dmatrices(formula_ml, data=test_df, return_type="dataframe")

#train_y = np.asarray(train_y).ravel()

#Logistic Regression
model = sm.Logit(train_y, train_x)
res = model.fit()

output = res.predict(test_x)
output = np.asanyarray(output).ravel()
output = np.round(output)
output_file = open("myLogit2.csv", "wb")
output_file_object = csv.writer(output_file)
output_file_object.writerow(["PassengerId", "Survived"])
output_file_object.writerows(zip(test_passengers, output))
output_file.close()


#Random Forest Classifier
'''
forest = RandomForestClassifier(n_estimators=100)
forest.fit(train_x, train_y)

output = forest.predict(test_x)
output = np.asanyarray(output).ravel()

output_file = open("myRandomForest3.csv", "wb")
output_file_object = csv.writer(output_file)
output_file_object.writerow(["PassengerId", "Survived"])
output_file_object.writerows(zip(test_passengers, output))
output_file.close()
'''
