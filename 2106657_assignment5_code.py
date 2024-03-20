# Necessary libraries
import numpy as np
import random

# parameters for size of grid
n = 6
m = 2

# returning how many cops occurred
total_cop = 0

# repeating a sufficient number of times
for j in range(0,10000):
    
# generating a grid with random entries and reshaping to be n x m
    possible_entries = np.arange(1,n*m+1,1)
    random.shuffle(possible_entries)
    grid = np.reshape(possible_entries, [n,m])
    
# a boolean for the loop to stop when a COP is no longer possible
    pp = True
    
# other argument to stop loop is if we have seen every item
    i = 1
    while pp == True and i < n*m:
        
# getting the index of the ith and i+1th entries
        ep1 = [np.argwhere(grid == i)[0,0],np.argwhere(grid == i)[0,1]]
        ep2 = [np.argwhere(grid == i+1)[0,0],np.argwhere(grid == i+1)[0,1]]
        
        
# generating an array of the ith entries neighbours to compare the i+1th to
# this is a rather brutish method but worked well 
        if ep1[0] > 0 and ep1[1] > 0:
            pn = [[ep1[0]+1,ep1[1]],[ep1[0],ep1[1]+1],[ep1[0]-1,ep1[1]],[ep1[0],ep1[1]-1]]
        
        elif ep1[0] > 0 and ep1[1] == 0:
            pn = [[ep1[0]+1,ep1[1]],[ep1[0],ep1[1]+1],[ep1[0]-1,ep1[1]]]
            
        elif ep1[0] == 0 and ep1[1] > 0:
            pn = [[ep1[0]+1,ep1[1]],[ep1[0],ep1[1]+1],[ep1[0],ep1[1]-1]]
                
        else:
            pn = [[ep1[0]+1,ep1[1]],[ep1[0],ep1[1]+1]]
        
# comparing all the neighbour indices to the i+1th 
        ind = 0
        
    # boolean to stop the large while loop as path no longer possible
        fc = False
        while ind < len(pn):
            if np.array_equal(pn[ind],ep2):
                ind = len(pn)
                fc = True
                
            else:
                ind = ind +1
                
        if fc == False:
            pp = False
            
        elif i == n*m-2:
            total_cop = total_cop+1
            pp = False
        
        else:
            i = i + 1
    
print(total_cop)
    
