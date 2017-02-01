# -*- coding: utf-8 -*-
"""
Created on Sat Oct 11 10:47:27 2014

@author: Karim
"""

import numpy as np
import pandas as pd

test_path = "test.csv"
train_path = "train.csv"

df = pd.read_csv(train_path, header=0)
dfTest = pd.read_csv(test_path, header=0)

#Clean Age
mean_age = np.mean(df.Age)
df.Age = df.fillna(mean_age)
df.Age = df.Age.astype(float)

#Clean_Sex
df["Gender"] = df.Sex.map({"female":0, "male":1}).astype(int)


#Clean Fare
df.Fare = df.Fare.map(lambda x: np.nan if x==0 else x)
class_means = df.pivot_table("Fare", columns="Pclass", aggfunc="mean")
df.Fare = df.Fare.map(lambda x: np.nan if x==0 else x)
df.Fare = df[["Fare", "Pclass"]].apply(lambda x: class_means[x["Pclass"]] if pd.isnull(x["Fare"]) else x["Fare"], axis=1)

print df.describe()
print df.info()
