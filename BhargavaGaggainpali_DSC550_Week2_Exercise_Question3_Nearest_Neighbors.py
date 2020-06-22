# File : BhargavaGaggainpali_DSC550_Week2_Exercise_Question3_Nearest_Neighbors.py
# Name : Bhargava Gaggainpali
# Date : JUN-21-2020
# Course : DSC550 - Data Mining
# Assignment :Week2_Exercise_Question3_Nearest_Neighbors


import random
import matplotlib.pyplot as pyplt

#define define_neighbors Function to create random uniform matrix
def define_neighbors(d):
    cube= []
    for x in range(len(d)):
        uniform = []
        for n in range(10000):
            uniform.append(random.uniform(0, 1))
        cube.append(uniform)
    return cube

#Calculate closest number from 0.5 in the list
def nearest(list, k=0.5):
    length=len(list)
    return list[min(range(length),key=lambda i: abs(list[i]-k))]

#Calculate farthest number from 0.5 in the list
def farthest(list, k=0.5):
    length=len(list)
    return list[max(range(length),key=lambda i: abs(list[i]-k))]

# function to get distances from closest and farthest point for each value of d
def get_nearest_neighbors(hypercube):
    near = []
    far = []
    for i in range(len(hypercube)):
        # Appending with absolute difference value from closest point
         near.append(abs(0.5-nearest(hypercube[i]))) 
        # Appending with absolute difference value from farthest point
         far.append(abs(0.5-farthest(hypercube[i])))   
    return near, far

# creating function for plot of nearest
def closest_plot(d, near):
    # Plot closest distances for each d
    pyplt.title('Distance from Closest point VS d')
    pyplt.plot(d, near)
    pyplt.xlabel('Dimension - d')
    pyplt.ylabel('Dist of nearest')
    pyplt.show()

# creating function for plot of farthest
def farthest_plot(d,far):
    # Plot farthest distances for each d
    pyplt.title('Distance from Farthest point VS d')
    pyplt.plot(d, far)
    pyplt.xlabel('Dimension - d')
    pyplt.ylabel('Dist of farthest')
    pyplt.show()

if __name__ == '__main__':
    try:
        #Define dimensions- 1 to 100
        d = [x for x in range(1, 100)]
        #call random matrix function
        hypercube = define_neighbors(d) 
        
        #Get the near and far elements from the matrix
        near, far = get_nearest_neighbors(hypercube) 
        #Call closest plot function for first plot         
        closest_plot(d, near)
        #Call Farthest plot function for second plot
        farthest_plot(d, far)
        print("Two Plots implemented") 
    except Exception as exception:
        print('exception')
        print('An exception of type {0} occurred.  Arguments:\n{1!r}'.format(type(exception).__name__, exception.args));
        