# -*- coding: utf-8 -*-
"""
Created on Mon Oct 13 15:13:51 2014

@author: Karim
"""

import numpy as np
import pandas as pd
import csv as csv
from sklearn.ensemble import RandomForestClassifier


train_path = "train.csv"
test_path = "test.csv"

#Clean Train df for Sex and Pclass
train_df = pd.read_csv(train_path, header=0)
train_df["Gender"] = train_df.Sex.map({"female":0, "male":1}).astype(int)
train_df["PclassCategory"] = train_df["Pclass"].apply(lambda x: 1 if x != 3 else 0).astype(int)

train_df["testCol"] = train_df["Gender"]
train_data = train_df[["Survived", "Gender", "PclassCategory"]].values

#print train_data[:5,:]

#Clean Test df for Sex ad Pclass
test_df = pd.read_csv(test_path, header=0)
test_df["Gender"] = test_df.Sex.map({"female":0, "male":1}).astype(int)
test_df["PclassCategory"] = test_df["Pclass"].apply(lambda x: 1 if x != 3 else 0).astype(int)

test_df["testCol"] = test_df["Gender"]
ids = test_df["PassengerId"].values

test_data = test_df[["Gender", "PclassCategory"]].values
print train_data


print "Training"
forest = RandomForestClassifier(n_estimators=100)
forest.fit(train_data[0::, 1::], train_data[0::,0])

print "Predicting"
output = forest.predict(test_data)

predictions_file = open("003.csv", "wb")
output_file_object = csv.writer(predictions_file)
output_file_object.writerow(["PassengerId", "Survived"])
output_file_object.writerows(zip(ids, output))
predictions_file.close()

print "Done!"

