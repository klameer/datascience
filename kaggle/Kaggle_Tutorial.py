# -*- coding: utf-8 -*-
"""
Created on Fri Oct 10 14:25:30 2014

@author: Karim
"""

import pandas as pd
import numpy as np

df = pd.read_csv("train.csv", header=0)

#Clean the data

#Clean fare
df.Fare = df.Fare.map(lambda x: np.nan if x==0 else x)
class_means = df.pivot_table("Fare", columns="Pclass", aggfunc="mean")
df.Fare = df[["Fare", "Pclass"]].apply(lambda x: class_means[x["Pclass"]] if pd.isnull(x["Fare"]) else x["Fare"], axis=1)

#df.Fare = df[['Fare', 'Pclass']].apply(lambda x: class_means[x['Pclass']] if pd.isnull(x['Fare']) else x['Fare'], axis=1)


print df.Fare[df.Fare==0]
print class_means