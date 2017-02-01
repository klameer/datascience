import numpy
import pandas
import statsmodels.api as sm

def simple_heuristic(file_path):
    myFile = pandas.read_csv(file_path)
    myFile.write_to_csv(file_path)

def testMe():
    print False or True and True

    
    


if __name__ == "__main__":
    testMe()
    
