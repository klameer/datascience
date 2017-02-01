# -*- coding: utf-8 -*-
"""
Created on Thu Oct 30 18:37:27 2014

@author: Karim
"""

import pandas as pd
import numpy as np
import csv as csv
import matplotlib.pylab as plt
import statsmodels.api as sm
from patsy import dmatrices

#Import data
train_path = "train.csv"
test_path = "test.csv"

train_data = pd.read_csv(train_path)
test_data = pd.read_csv(test_path)

#Data Analysis
#Age Plot

for i in range(1,4):
    train_data[train_data["Pclass"] == i]["Age"].dropna().plot(kind="kde")
plt.title("Age Disribution within classes")
plt.legend(("1st Class", "2nd Class", "3rd Class"), loc="best")
plt.xlabel("Age")
plt.ylabel("Density")
plt.savefig("ageclassdist.png", format="png")


#Cleaning the data
#Clean Age

median_ages = np.zeros(3)

for i in range(1,4):
    median_ages[i-1] = train_data[train_data.Pclass == i]["Age"].dropna().median()
    
for i in range(1,4):
    train_data.loc[(train_data.Pclass == i) & (train_data.Age.isnull()), "Age"] = median_ages[i-1]
    test_data.loc[(test_data.Pclass == i) & (test_data.Age.isnull()), "Age"] = median_ages[i-1]

train_data_final = train_data[["Survived", "Pclass", "Sex", "Age", "SibSp", "Parch"]]
test_data_final = test_data[["Pclass", "Sex", "Age", "SibSp", "Parch"]]
test_data_final["Survived"] = 1


#Setting up the model
formula_ml = "Survived ~ C(Pclass) + C(Sex) + Age + SibSp + Parch"
train_y, train_x = dmatrices(formula_like=formula_ml, data=train_data_final, return_type="dataframe")
test_y, test_x = dmatrices(formula_like=formula_ml, data=test_data_final, return_type="dataframe")
logit_model = sm.Logit(train_y, train_x)
res = logit_model.fit()
output = res.predict(test_x)
output = np.asanyarray(output).ravel()
output = np.round(output)

output_file = open("Logit.csv", "wb")
output_file_object = csv.writer(output_file)
output_file_object.writerow(["PassengerId", "Survived"])
output_file_object.writerows(zip(test_data["PassengerId"], output))
output_file.close()
