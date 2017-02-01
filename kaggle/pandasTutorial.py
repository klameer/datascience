# -*- coding: utf-8 -*-
"""
Created on Tue Oct 07 16:38:17 2014

@author: Karim
"""

import numpy as np
import csv as csv
import pandas as pd

def main():
   df = pd.read_csv("train.csv", header=0) 
   print df.head(3)
    
    
    
if __name__=="__main__":main()