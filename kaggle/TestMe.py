# -*- coding: utf-8 -*-
"""
Created on Mon Oct 06 16:53:24 2014

@author: Karim
"""

def main():
    number_of_classes = 4
    number_of_fare_buckets = 3
    
    for i in xrange(number_of_classes):
        for j in xrange(number_of_fare_buckets):
            print "i = %s | j = %s" % (i, j)


if __name__=="__main__":main()