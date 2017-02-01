# -*- coding: utf-8 -*-
"""
Created on Mon Feb 02 10:03:36 2015

@author: Karim
"""

import sqlite3
import pandas as pd

df = pd.DataFrame(columns=("Letter", "Number"))
df = df.append(pd.Series({"Letter":"A", "Number":1}), ignore_index=True)
df = df.append(pd.Series({"Letter":"B", "Number":2}), ignore_index=True)
df = df.append(pd.Series({"Letter":"C", "Number":3}), ignore_index=True)

