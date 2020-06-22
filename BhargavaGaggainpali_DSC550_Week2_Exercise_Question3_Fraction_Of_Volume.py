# File : BhargavaGaggainpali_DSC550_Week2_Exercise_Question3_Fraction_Of_Volume.py
# Name : Bhargava Gaggainpali
# Date : JUN-21-2020
# Course : DSC550 - Data Mining
# Assignment :Week2_Exercise_Question3_Fraction_Of_Volume


import matplotlib.pyplot as pyplt
from scipy.special import gamma
from math import pi

# Defining variables 
fraction_of_points_arr=[]
fraction_of_points_arr_for_thin_sphere=[]

d=[x for x in range(1,100)] 
dim=[y for y in range(1,400)] 

def volume(d):  
    for i in d:
        # if r=1 then the formula of the volume of the sphere is (pi**i/2)/gamma(i/2+1)
        volume=(pi**i/2)/gamma(i/2+1)
        fraction_of_points_arr.append(volume)

def volume_thin_shell(dim): 
    for i in dim:   
        l=2
        e=0.01
        r=l/2
        # with the higher dimention it goes to 1
        volume_thinshell=1-(1-e/r)**i
        fraction_of_points_arr_for_thin_sphere.append(volume_thinshell)

# function for plot
def plot_one(d,fraction_of_point):
    pyplt.plot(d, fraction_of_point)
    pyplt.xlabel("d")
    pyplt.ylabel("Fraction Of point")
    pyplt.show()

def plot_two(d,fraction_of_point_of_thin_sphere):
    pyplt.plot(d, fraction_of_point_of_thin_sphere)
    pyplt.xlabel("d")
    pyplt.ylabel("Fraction Of point of thin shell")
    pyplt.show()
print(fraction_of_points_arr_for_thin_sphere)

if __name__=='__main__':
    #calling function inside the try block to catch the errors
    try:
        volume(d)
        volume_thin_shell(dim)

        plot_one(d,fraction_of_points_arr)
        plot_two(dim,fraction_of_points_arr_for_thin_sphere)
    except Exception as exception:
        print('An exception of type {0} occurred.  Arguments:\n{1!r}'.format(type(exception).__name__, exception.args));