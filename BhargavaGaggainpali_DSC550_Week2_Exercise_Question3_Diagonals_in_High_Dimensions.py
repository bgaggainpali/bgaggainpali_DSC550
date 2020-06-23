# File : BhargavaGaggainpali_DSC550_Week2_Exercise_Question3_Diagonals_in_High_Dimensions.py
# Name : Bhargava Gaggainpali
# Date : JUN-21-2020
# Course : DSC550 - Data Mining
# Assignment :Week2_Exercise_Question3_Diagonals_in_High_Dimensions


import numpy as np
import math
import matplotlib.pyplot as matplt
from scipy import stats
from collections import Counter

# creating class counter for PMF calculation.
class PMF(Counter):
# normalizing pmf to add probabalities by 1
    def normalize(self):
        s = float(sum(self.values()))
        for key in self:
            self[key] /=s
    
#Function to get the array of angles for d-dimensions
def get_angle_in_d(n, d):
    results = np.zeros(n)
    for i in range(0,n):
        points_pre = np.random.rand(2, d)   
        points_pre[points_pre <= 0.5] = -1
        points_pre[points_pre > 0.5] = 1
        cos_theta = np.dot(points_pre[0], points_pre[1])/(np.linalg.norm(points_pre[0])*np.linalg.norm(points_pre[1])) 
        # convert angle to degree
        results[i] = round(math.degrees(math.acos(cos_theta)), 2)  
    return results

# creating function for plot
def plot(angle): 
    p = PMF(angle)
    p.normalize()
    key_arr = []
    prob_arr = []
    for key, prob in p.items():
        key_arr.append(key)
        prob_arr.append(prob)
    matplt.hist(prob_arr, bins=20)
    matplt.xlabel('Size')
    matplt.ylabel('EPMF Values')
    matplt.show()


if __name__ == '__main__':
    d=10
    for i in range(1,4):
        ang = get_angle_in_d(100000, d)
        plot(ang)
        summary=stats.describe(ang)   
        print('summary for d =',d,'\n',summary, '\n')
        d*=10
        
    print('with increase in dimensions, the angle becomes 90.'
          'Digonalvectors will become perpendicular to the cordinates axes'
          'It will have 2**d corners and 2**d diagonal vectors from the origin to the corners'
          'in d-dim hypercube')