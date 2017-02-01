# -*- coding: utf-8 -*-
"""
Created on Fri Oct 24 21:54:29 2014

@author: Karim
"""
import pandas as pd

def predict_survived(pclass=None,
                     HotSex=None,
                     age=None,
                     sibsp=None,
                     parch=None):
    """ Predictor for Survived from model/544ab84c99fca410fd0013cb

        Predictive model by BigML - Machine Learning Made Easy
    """
    if (HotSex is None):
        return u'0'
    if (HotSex == 1):
        if (pclass is None):
            return u'0'
        if (pclass > 1):
            if (age is None):
                return u'0'
            if (age > 12.83333):
                if (age > 33.39312):
                    if (sibsp is None):
                        return u'0'
                    if (sibsp > 0):
                        return u'0'
                    if (sibsp <= 0):
                        if (age > 45.25):
                            if (age > 61.5):
                                if (age > 63.5):
                                    return u'0'
                                if (age <= 63.5):
                                    return u'1'
                            if (age <= 61.5):
                                return u'0'
                        if (age <= 45.25):
                            if (age > 43.5):
                                return u'0'
                            if (age <= 43.5):
                                if (pclass > 2):
                                    if (age > 38.5):
                                        if (age > 39.5):
                                            return u'0'
                                        if (age <= 39.5):
                                            return u'0'
                                    if (age <= 38.5):
                                        return u'0'
                                if (pclass <= 2):
                                    if (age > 40.5):
                                        return u'0'
                                    if (age <= 40.5):
                                        if (age > 34.5):
                                            return u'0'
                                        if (age <= 34.5):
                                            return u'0'
                if (age <= 33.39312):
                    if (age > 30.75):
                        if (age > 32.25):
                            return u'0'
                        if (age <= 32.25):
                            if (parch is None):
                                return u'0'
                            if (parch > 0):
                                return u'0'
                            if (parch <= 0):
                                if (sibsp is None):
                                    return u'0'
                                if (sibsp > 1):
                                    return u'0'
                                if (sibsp <= 1):
                                    if (pclass > 2):
                                        if (sibsp > 0):
                                            return u'0'
                                        if (sibsp <= 0):
                                            if (age > 31.5):
                                                return u'0'
                                            if (age <= 31.5):
                                                return u'0'
                                    if (pclass <= 2):
                                        if (sibsp > 0):
                                            return u'1'
                                        if (sibsp <= 0):
                                            return u'0'
                    if (age <= 30.75):
                        if (pclass > 2):
                            if (age > 24.75):
                                if (sibsp is None):
                                    return u'0'
                                if (sibsp > 0):
                                    if (age > 25.5):
                                        return u'0'
                                    if (age <= 25.5):
                                        return u'0'
                                if (sibsp <= 0):
                                    if (age > 27.5):
                                        if (age > 28.75):
                                            if (age > 29.5):
                                                return u'0'
                                            if (age <= 29.5):
                                                return u'0'
                                        if (age <= 28.75):
                                            return u'0'
                                    if (age <= 27.5):
                                        if (age > 26.5):
                                            return u'1'
                                        if (age <= 26.5):
                                            if (age > 25.5):
                                                return u'0'
                                            if (age <= 25.5):
                                                return u'0'
                            if (age <= 24.75):
                                if (sibsp is None):
                                    return u'0'
                                if (sibsp > 1):
                                    return u'0'
                                if (sibsp <= 1):
                                    if (age > 20.25):
                                        if (sibsp > 0):
                                            return u'0'
                                        if (sibsp <= 0):
                                            if (age > 23.75):
                                                return u'0'
                                            if (age <= 23.75):
                                                if (age > 22.5):
                                                    return u'0'
                                                if (age <= 22.5):
                                                    if (age > 20.75):
                                                        return u'0'
                                                    if (age <= 20.75):
                                                        return u'0'
                                    if (age <= 20.25):
                                        if (age > 19.5):
                                            if (sibsp > 0):
                                                return u'1'
                                            if (sibsp <= 0):
                                                return u'0'
                                        if (age <= 19.5):
                                            if (sibsp > 0):
                                                return u'0'
                                            if (sibsp <= 0):
                                                if (age > 16.5):
                                                    if (age > 17.5):
                                                        if (age > 18.5):
                                                            return u'0'
                                                        if (age <= 18.5):
                                                            return u'0'
                                                    if (age <= 17.5):
                                                        return u'0'
                                                if (age <= 16.5):
                                                    return u'0'
                        if (pclass <= 2):
                            if (age > 20):
                                return u'0'
                            if (age <= 20):
                                if (age > 18.5):
                                    return u'0'
                                if (age <= 18.5):
                                    return u'0'
            if (age <= 12.83333):
                if (sibsp is None):
                    return u'1'
                if (sibsp > 2):
                    if (age > 3.5):
                        return u'0'
                    if (age <= 3.5):
                        if (age > 2.5):
                            return u'1'
                        if (age <= 2.5):
                            return u'0'
                if (sibsp <= 2):
                    if (age > 10):
                        if (age > 11.5):
                            return u'1'
                        if (age <= 11.5):
                            return u'0'
                    if (age <= 10):
                        return u'1'
        if (pclass <= 1):
            if (age is None):
                return u'0'
            if (age > 52.91667):
                if (age > 75.5):
                    return u'1'
                if (age <= 75.5):
                    if (age > 60.5):
                        return u'0'
                    if (age <= 60.5):
                        if (sibsp is None):
                            return u'0'
                        if (sibsp > 0):
                            return u'1'
                        if (sibsp <= 0):
                            if (age > 55.5):
                                return u'0'
                            if (age <= 55.5):
                                return u'0'
            if (age <= 52.91667):
                if (age > 14.25):
                    if (age > 22.5):
                        if (age > 36.5):
                            if (age > 47.5):
                                if (parch is None):
                                    return u'1'
                                if (parch > 0):
                                    return u'0'
                                if (parch <= 0):
                                    if (age > 49.5):
                                        if (age > 50.5):
                                            return u'1'
                                        if (age <= 50.5):
                                            if (sibsp is None):
                                                return u'0'
                                            if (sibsp > 1):
                                                return u'1'
                                            if (sibsp <= 1):
                                                return u'0'
                                    if (age <= 49.5):
                                        return u'1'
                            if (age <= 47.5):
                                if (age > 45.25):
                                    return u'0'
                                if (age <= 45.25):
                                    if (sibsp is None):
                                        return u'0'
                                    if (sibsp > 1):
                                        return u'0'
                                    if (sibsp <= 1):
                                        if (sibsp > 0):
                                            if (age > 43.5):
                                                return u'0'
                                            if (age <= 43.5):
                                                return u'1'
                                        if (sibsp <= 0):
                                            if (age > 39.5):
                                                return u'0'
                                            if (age <= 39.5):
                                                return u'0'
                        if (age <= 36.5):
                            if (age > 33.5):
                                if (age > 35.5):
                                    return u'1'
                                if (age <= 35.5):
                                    return u'1'
                            if (age <= 33.5):
                                if (age > 28.5):
                                    return u'0'
                                if (age <= 28.5):
                                    if (parch is None):
                                        return u'1'
                                    if (parch > 1):
                                        return u'0'
                                    if (parch <= 1):
                                        if (age > 24.5):
                                            if (age > 27.5):
                                                if (sibsp is None):
                                                    return u'0'
                                                if (sibsp > 0):
                                                    return u'0'
                                                if (sibsp <= 0):
                                                    return u'1'
                                            if (age <= 27.5):
                                                return u'1'
                                        if (age <= 24.5):
                                            if (age > 23.5):
                                                return u'0'
                                            if (age <= 23.5):
                                                return u'1'
                    if (age <= 22.5):
                        if (age > 17.5):
                            return u'0'
                        if (age <= 17.5):
                            return u'1'
                if (age <= 14.25):
                    return u'1'
    if (HotSex != 1):
        if (pclass is None):
            return u'1'
        if (pclass > 2):
            if (sibsp is None):
                return u'0'
            if (sibsp > 2):
                if (age is None):
                    return u'0'
                if (age > 16.5):
                    return u'1'
                if (age <= 16.5):
                    if (age > 5.5):
                        return u'0'
                    if (age <= 5.5):
                        if (age > 4):
                            return u'1'
                        if (age <= 4):
                            return u'0'
            if (sibsp <= 2):
                if (age is None):
                    return u'1'
                if (age > 38.5):
                    if (age > 55.5):
                        return u'1'
                    if (age <= 55.5):
                        return u'0'
                if (age <= 38.5):
                    if (age > 7):
                        if (age > 11.5):
                            if (age > 16.5):
                                if (sibsp > 1):
                                    return u'0'
                                if (sibsp <= 1):
                                    if (parch is None):
                                        return u'0'
                                    if (parch > 1):
                                        return u'1'
                                    if (parch <= 1):
                                        if (age > 17.5):
                                            if (age > 27.5):
                                                if (age > 29.5):
                                                    if (age > 36.5):
                                                        return u'0'
                                                    if (age <= 36.5):
                                                        if (age > 33.5):
                                                            return u'1'
                                                        if (age <= 33.5):
                                                            if (age > 31.5):
                                                                return u'0'
                                                            if (age <= 31.5):
                                                                return u'0'
                                                if (age <= 29.5):
                                                    return u'0'
                                            if (age <= 27.5):
                                                if (age > 26.5):
                                                    return u'1'
                                                if (age <= 26.5):
                                                    if (sibsp > 0):
                                                        return u'0'
                                                    if (sibsp <= 0):
                                                        if (age > 25.5):
                                                            return u'1'
                                                        if (age <= 25.5):
                                                            if (age > 23.5):
                                                                return u'0'
                                                            if (age <= 23.5):
                                                                if (age > 21.5):
                                                                    return u'1'
                                                                if (age <= 21.5):
                                                                    if (age > 19.5):
                                                                        return u'0'
                                                                    if (age <= 19.5):
                                                                        return u'1'
                                        if (age <= 17.5):
                                            return u'0'
                            if (age <= 16.5):
                                if (age > 14.75):
                                    return u'1'
                                if (age <= 14.75):
                                    if (age > 13.5):
                                        return u'0'
                                    if (age <= 13.5):
                                        return u'1'
                        if (age <= 11.5):
                            return u'0'
                    if (age <= 7):
                        if (age > 3):
                            return u'1'
                        if (age <= 3):
                            return u'1'
        if (pclass <= 2):
            if (age is None):
                return u'1'
            if (age > 3.33333):
                if (age > 22.73333):
                    if (pclass > 1):
                        if (age > 56):
                            return u'0'
                        if (age <= 56):
                            if (age > 27.5):
                                if (age > 37):
                                    if (age > 39):
                                        if (sibsp is None):
                                            return u'1'
                                        if (sibsp > 0):
                                            return u'1'
                                        if (sibsp <= 0):
                                            return u'1'
                                    if (age <= 39):
                                        return u'0'
                                if (age <= 37):
                                    return u'1'
                            if (age <= 27.5):
                                if (age > 25.5):
                                    if (age > 26.5):
                                        return u'1'
                                    if (age <= 26.5):
                                        return u'0'
                                if (age <= 25.5):
                                    if (parch is None):
                                        return u'1'
                                    if (parch > 0):
                                        return u'1'
                                    if (parch <= 0):
                                        return u'1'
                    if (pclass <= 1):
                        if (parch is None):
                            return u'1'
                        if (parch > 1):
                            return u'1'
                        if (parch <= 1):
                            if (age > 49.5):
                                if (age > 50.5):
                                    return u'1'
                                if (age <= 50.5):
                                    if (parch > 0):
                                        return u'1'
                                    if (parch <= 0):
                                        return u'0'
                            if (age <= 49.5):
                                return u'1'
                if (age <= 22.73333):
                    return u'1'
            if (age <= 3.33333):
                if (pclass > 1):
                    return u'1'
                if (pclass <= 1):
                    return u'0'                    

df = pd.read_csv("test.csv", header=0)
df["HotSex"] = df["Sex"].map({"female":0, "male":1}).astype(int)

predict_survived(pclass=df.Pclass, HotSex=df.HotSex, age=df.Age, sibsp=df.SibSp, parch=df.Parch)
