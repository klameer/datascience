# -*- coding: utf-8 -*-
"""
Created on Fri Oct 10 14:25:30 2014

@author: Karim
"""

import pandas as pd
import numpy as np
import matplotlib.pylab  as plt


df = pd.read_csv("train.csv", header=0)

def cleandf(df):
    #Clean the data
    
    #Clean fare
    df.Fare = df.Fare.map(lambda x: np.nan if x==0 else x)
    class_means = df.pivot_table("Fare", columns="Pclass", aggfunc="mean")
    df.Fare = df[["Fare", "Pclass"]].apply(lambda x: class_means[x["Pclass"]] \
    if pd.isnull(x["Fare"]) else x["Fare"], axis=1)
    
    #Cean age
    meanAge = np.mean(df.Age)
    df.Age = df.Age.fillna(meanAge)
    
    #Clean Embarked
    df.Cabin = df.Cabin.fillna("Unknown")
    modeEmbarked = mode(df.Embarked)[0][0]
    df.Embarked = df.Embarked.fillna(modeEmbarked)
    return df
    
def cleanddf(no_bins=0):
    #you'll want to tweak this to conform with your computer's file system
    trainpath = 'train.csv'
    testpath = 'test.csv'
    traindf = pd.read_csv(trainpath)
    testdf = pd.read_csv(testpath)
    
    #discretise fare
    if no_bins==0:
        return [cleandf(traindf), cleandf(testdf)]
    traindf=cleandf(traindf)
    testdf=cleandf(testdf)
    bins_and_binned_fare = pd.qcut(traindf.Fare, no_bins, retbins=True)
    bins=bins_and_binned_fare[1]
    traindf.Fare = bins_and_binned_fare[0]
    testdf.Fare = pd.cut(testdf.Fare, bins)
    
    #discretise age
    bins_and_binned_age = pd.qcut(traindf.Age, no_bins, retbins=True)
    bins=bins_and_binned_age[1]
    
    traindf.Age = bins_and_binned_age[0]
    testdf.Age = pd.cut(testdf.Age, bins)
    
    #create a submission file for kaggle
    predictiondf = pd.DataFrame(testdf['PassengerId'])
    predictiondf['Survived']=[0 for x in range(len(testdf))]
    predictiondf.to_csv('C:/Documents and Settings/DIGIT/My Documents/Google Drive/Blogs/triangleinequality/Titanic/prediction.csv',
                  index=False)
    return [traindf, testdf]

def proportionSurvived(discreteVar):
    by_var = traindf.groupby([discreteVar,'Survived'])
    table = by_var.size()
    table = table.unstack()
    normedtable = table.div(table.sum(1), axis=0)
    return normedtable

discreteVarList = ["Sex", "Pclass", "Embarked"]
fig1, axes1 = plt.subplots(3,1)
for i in range(3):
    var = discreteVarList[i]
    table = proportionSurvived(var)
    table.plot(kind='barh', stacked=True, ax=axes1[i])
    
fig1.show()
