import random
import math
import numpy as np
import matplotlib.pyplot as plt

"""Below function runs on the basis of Marsaglia Polar form which is a method 
for generating a pair of independent standard normal random variables. This function returns a tuple of Independent gaussian pair"""
def NormalPair():
    x = 0  #intialisation of (x,y) in polar form 
    y = 0
    m = 1  #initialization of m
    while(m>=1 or m==0):
        x = random.uniform(0,1)
        y = random.uniform(0,1)  # x and y are uniformly distributed in (0,1)
        a = 2*x-1
        b = 2*y-1
        m = a**2 + b**2  
    ans = math.sqrt(-2.0 * math.log(m) / m) #marsaglia formula which much more efficient than Box-Muller Algorithm
    n1 = a * ans
    n2 = b * ans
    return n1, n2 # returns a tuple of normally distributed or gaussian pair

if __name__ == "__main__":
    x=[]
    for i in range(0,100000):
        l=NormalPair()
        x.append(l[0])
        x.append(l[1])
        #print(x)
    #print(x.shape)
    x=np.array(x)
    plt.hist(x)
    plt.show()
    plt.savefig('NormalDistribution') #please check in the current directory for the image
    #fig.savepng('NormalDistribution')
    """ Uncomment this to print user inputted number of gaussian pairs.
     beaware of indentation errors!!!
     n=int(input())
     for i in range(0,n):
         print(NormalPair())
     ON each run the program prints various gaussian pairs """
    