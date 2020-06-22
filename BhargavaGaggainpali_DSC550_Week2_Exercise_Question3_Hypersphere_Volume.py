# File : BhargavaGaggainpali_DSC550_Week2_Exercise_Question3_Hypersphere_Volume.py
# Name : Bhargava Gaggainpali
# Date : JUN-21-2020
# Course : DSC550 - Data Mining
# Assignment :Week2_Exercise_Question3_Hypersphere_Volume

import matplotlib.pyplot as pyplt
from math import pi
from scipy.special import gamma

# Create a list to store calculated volume values
volume_list=[]
#Defining dimension for the plot    
d=[x for x in range(1,51)]
#radius is 1 as it is unit radius
r=1

#function to calculate volume
def calculate_volume(value):
    return (pi**value/2/gamma(value/2+1))*r**value
    
# calculating the volume of the hypersphere with range(1,50) dimensions
for i in range(1,51):
        # Calculate volume
        volume_val=calculate_volume(i)
        #insert into the volume_val
        volume_list.append(volume_val)

print(volume_list)

# Plot using matplotlib
pyplt.plot(d,volume_list)
pyplt.xlabel("dim")
pyplt.ylabel("Volume")
pyplt.show()