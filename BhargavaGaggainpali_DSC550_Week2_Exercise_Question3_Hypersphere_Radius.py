# File : BhargavaGaggainpali_DSC550_Week2_Exercise_Question3_Hypersphere_Radius.py
# Name : Bhargava Gaggainpali
# Date : JUN-21-2020
# Course : DSC550 - Data Mining
# Assignment :Week2_Exercise_Question3_Hypersphere_Radius


import matplotlib.pyplot as pyplt
from scipy.special import gamma
from math import pi

# Calculate the radius using volume
radius_list=[]
#Define dimension for the plot    
d=[x for x in range(1,101)]
v=1

def calculate_radius(value):
    return gamma((value/2+1)**1/value)/pi**0.5*v**1/value
    
# hypersphere dimension range is 1 to 100
for i in range(1,101):
    rad=calculate_radius(i)
    radius_list.append(rad)
    
print(radius_list)


pyplt.plot(d,radius_list)
pyplt.xlabel("dim")
pyplt.ylabel("Volume")
pyplt.show()