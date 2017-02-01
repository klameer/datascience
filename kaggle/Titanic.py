# -*- coding: utf-8 -*-
"""
Created on Sun Oct 05 20:49:00 2014

@author: Karim
"""

import csv as csv
import numpy as np

def genderModel2():
    csv_file_object = csv.reader(open("train.csv", "rb"))
    header = csv_file_object.next()
    data = []
    
    for row in csv_file_object:
        data.append(row)
    
    data = np.array(data)
    fare_ceiling = 40
    #change data in fare column to have a maximum of 39
    data[data[0::,9].astype(np.float) >= fare_ceiling, 9] = fare_ceiling - 1.0
    
    fare_bracket_size = 10
    number_of_price_brackets = fare_ceiling / fare_bracket_size
    number_of_classes = len(np.unique(data[0::, 2]))
    
    survival_table = np.zeros([2,number_of_classes,number_of_price_brackets],float)
    for i in xrange(number_of_classes):
        for j in xrange(number_of_price_brackets):
            women_only_stats = data[(data[0::, 4] == "female") \
            & (data[0::, 2].astype(np.float) == i+1) \
            & (data[0::, 9].astype(np.float) >= j * fare_bracket_size) \
            & (data[0::, 9] < (j+1) * fare_bracket_size), 1]

            men_only_stats = data[(data[0::, 4] != "female") \
            & (data[0::, 2].astype(np.float) == i+1) \
            & (data[0::, 9].astype(np.float) >= j * fare_bracket_size) \
            & (data[0::, 9] < (j+1) * fare_bracket_size), 1]
            
            survival_table[0, i, j] = np.mean(women_only_stats.astype(np.float))
            survival_table[1, i, j] = np.mean(men_only_stats.astype(np.float))
            
            


            
    survival_table[survival_table != survival_table] = 0
    survival_table[survival_table < 0.5] = 0
    survival_table[survival_table >= 0.5] = 1
    
    test_file = open('test.csv', 'rb')
    test_file_object = csv.reader(test_file)    
    header = test_file_object.next()
    
    predictions_file = open("GenderClassModel2.csv", "wb")
    predictions_file_object = csv.writer(predictions_file)
    predictions_file_object.writerow(["PassengerId","Survived"])
    
    for row in test_file_object:
        for j in xrange(number_of_price_brackets):
            # If there is no fare then place the price of the ticket according to class
            try:
                row[8] = float(row[8])    # No fare recorded will come up as a string so
                                          # try to make it a float
            except:                       # If fails then just bin the fare according to the class
                bin_fare = 3 - float(row[1])
                break                     # Break from the loop and move to the next row
            if row[8] > fare_ceiling:     # Otherwise now test to see if it is higher
                                          # than the fare ceiling we set earlier
                bin_fare = number_of_price_brackets - 1
                break                     # And then break to the next row
    
            if row[8] >= j*fare_bracket_size\
                and row[8] < (j+1)*fare_bracket_size:     # If passed these tests then loop through
                                                          # each bin until you find the right one
                                                          # append it to the bin_fare
                                                          # and move to the next loop
                bin_fare = j
                break
            # Now I have the binned fare, passenger class, and whether female or male, we can
            # just cross ref their details with our survival table
        if row[3] == 'female':
            predictions_file_object.writerow([row[0], "%d" % int(survival_table[ 0, float(row[1]) - 1, bin_fare ])])
        else:
            predictions_file_object.writerow([row[0], "%d" % int(survival_table[ 1, float(row[1]) - 1, bin_fare])])
    
    # Close out the files
    test_file.close()
    predictions_file.close()            
    


def explore():
    train_file = open("train.csv", "rb")
    train_file_object = csv.reader(train_file)
    header = train_file_object.next()
    data = []
    
    for row in train_file_object:
        data.append(row)
    data = np.array(data)
    
    #Stats
    number_passengers = np.size(data[0::,1].astype(np.float))
    number_survived = np.sum(data[0::,1].astype(np.float))

    women_only_stats = data[0::,4] == "female"
    men_only_stats = data[0::, 4] != "female"
    

    women_onboard = data[women_only_stats,1].astype(np.float)
    men_onboard = data[men_only_stats, 1].astype(np.float)
    
    fare_ceiling = 40
    data[data[0::,9].astype(np.float) >= fare_ceiling, 9] = fare_ceiling - 1.0
    fare_bracket_size = 10
    number_of_price_brackets = fare_ceiling / fare_bracket_size
    number_of_classes = len(np.unique(data[0::,2]))
    
    survival_table = np.zeros((2, number_of_classes, number_of_price_brackets))
    
    for i in xrange(number_of_classes):             #loop through each class
        for j in xrange(number_of_price_brackets):  #loop through each bin
            women_only_stats = data[(data[0::,4] == "female")
            & (data[0::,2].astype(np.float) == i+1)
            & (data[0::,9].astype(np.float) >= j*fare_bucket_size)
            & (data[0::,9].astype(np.float) < (j+1)*fare_bucket_size), 1 ]
            
            men_only_stats = data[(data[0::,4] != "female")    #is a male
                           &(data[0::,2].astype(np.float) #and was ith class
                                 == i+1)                                       
                           &(data[0:,9].astype(np.float)  #was greater 
                                >= j*fare_bracket_size)   #than this bin              
                           &(data[0:,9].astype(np.float)  #and less than
                                < (j+1)*fare_bracket_size)#the next bin    
                              , 1] 

            survival_table[0,i,j] = np.mean(women_only_stats.astype(np.float))
            survival_table[1,i,j] = np.mean(men_only_stats.astype(np.float))

    survival_table[survival_table != survival_table] = 0
    survival_table[survival_table < 0.5] = 0
    survival_table[survival_table >= 0.5] = 1
    
    print survival_table
    
    
    '''
    print data[women_only_stats, 0::]

    print "Number of passengers %s" % number_passengers
    print "Number of passengers survived %s" % number_survived
    
    print "-------------------------"
    print "Number of Women passengers %s" % np.size(women_only_stats)
    '''    
    
    '''print header
    print data
    print "Done!"
    '''
    train_file.close()
    

def genderBasedModel():
    test_file = open("test.csv","rb")
    prediction_file = open("genderbasedmodel.csv", "wb")
    
    
    test_file_object = csv.reader(test_file)
    prediction_file_object = csv.writer(prediction_file)
    
    header = test_file_object.next()
    prediction_file_object.writerow(["PassengerId", "Survived"])
    
    for row in test_file_object:
        if row[3] == "female":
            prediction_file_object.writerow([row[0], '1'])
        else:
            prediction_file_object.writerow([row[0], '0'])
    
    test_file.close()
    prediction_file.close()
    print "Done"    
        
    
if __name__== "__main__":genderModel2()
    
    