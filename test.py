import os
import datetime
import pathlib

def test_test():
    test = ['d','f','g']
    for i in range(2):
        for j in range(10):
            test.append(j)
    print(test)
    return(test)

def sorted():
    res=[]
    ar=test_test()
    for i in ar:
        if i not in res:
                res.append(i)
    print(res)
        
     
if __name__ == '__main__':
   sorted()
   