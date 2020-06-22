# File : BhargavaGaggainpali_DSC550_Week2_Exercise_Question2_Non_Derivable_Itemsest.py
# Name : Bhargava Gaggainpali
# Date : JUN-21-2020
# Course : DSC550 - Data Mining
# Assignment :Week2_Exercise_Question2_Non_Derivable_Itemsest


import pandas as pd
from itertools import combinations

#Get the subsets
def subsets_comb(itemset, num_comb):
    combinations_arr = []
    for c in combinations(itemset, num_comb):
        combinations_arr.append(c)
    return combinations_arr

#Extract the combinations from the itemsets
def calc_comb(st, itemset, dictionary, n):
    value = 0.0
    for num in range(n-1, 0, -1):
        subsets = subsets_comb(itemset, num)
        for c in subsets:
            comb_set = all(item in c for item in st)
            if comb_set or st == ():
                i = int(dictionary[c]) * pow(-1.0, (n+1) - num)
                value += i
    if st == ():
        empty = 0
        for dictval in dictionary.values():
            empty += int(dictval)
        value += empty * pow(-1.0, (n+1))
    return value

#Check if it is derivable or not  
def check_derivable(lower_bound,upper_bound):
    # Check if derivable or not
    if lower_bound == upper_bound:
        bound = 'Derivable'
    else:
        bound = 'Non-Derivable'
    return bound
    
# Get the upper and lower bounds 
def calc_bounds(itemset, d):
    # set variables to obtain and determin upper and lower bound per itemset
    ub_arr = []
    lb_arr = []
    lb = 0
    ub = 0
    length = len(itemset)
    
    # Break the combinations to subsets
    for index in range(length):
        #Get the subsets
        subsets = subsets_comb(itemset, index)
        
        # Odd or Even conditions 
        boolean_Odd = (length - len(subsets[0]))%2
        for comb in subsets:
            # if length is odd then change upper bound list
            if boolean_Odd:
                ub_arr.append(calc_comb(comb, itemset, d, length))
            # if length is even, change lower bound list
            else:
                lb_arr.append(calc_comb(comb, itemset, d, length))
                
    # if the maximum number in lower bound array is negative,set it to zero
    if max(lb_arr) < 0:
        lb = 0
    # if maxium number >= greater, set lower bound to that value
    else:
        lb = max(lb_arr)
    
    # set upper bound to minumum of ub_arr
    ub = min(ub_arr)
    
    #Check if it is derivable or not
    der=check_derivable(lb, ub)
    
    return '{}: [{}, {}] - {}'.format(itemset, lb, ub, der)    

if __name__=='__main__':
    try:
        # reading data from the input files
        ndi_df = pd.read_csv('ndi.txt', header = None)
        itemset_df = pd.read_csv('itemsets.txt', header = None)
        # Getting the dicts
        itemset_dict = {}
        for i, itemset_support in enumerate(itemset_df[0]):
            support_arr=[] 
            # splitting
            for val in itemset_support.split(' '):
                #As per question -hypen format
                if val == '-': 
                    continue
                else:
                    support_arr.append(val)              
            itemset_dict[tuple(support_arr[:-1])] = support_arr[-1]
        # ndi.txt file datasets
        ndi_dict = {}
        for i, itemset in enumerate(ndi_df[0]):
            ndi_dict[i] = itemset.split(' ')
        for itemset in ndi_dict.values():
            print(calc_bounds(itemset, itemset_dict))
    except Exception as exception:
        print('An exception of type {0} occurred.  Arguments:\n{1!r}'.format(type(exception).__name__, exception.args)); 