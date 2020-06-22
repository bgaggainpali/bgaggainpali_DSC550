# File : BhargavaGaggainpali_DSC550_Week2_Exercise_Question1_Closed_ Itemset_Mining.py
# Name : Bhargava Gaggainpali
# Date : JUN-21-2020
# Course : DSC550 - Data Mining
# Assignment :Week2_Exercise_Question1_Closed_ Itemset_Mining


import pandas as pd

file_name="mushroom.txt"

#Function to create database for the given itemset
def create_database(itemset):
    return pd.Series(itemset).str.join('|').str.get_dummies()

#define a function for Charm Algorithm
def charm_alg(minsup):
    print("Filename-",file_name,"Minsup value-",minsup)
    values_freq = []
    for col in database.columns:
        sup=database[col].sum()
        if sup >= minsup:
            values_freq.append(int(col))
        else:
            pass
#Print the values that are greater than the minusp given
    print('There are %d items with frequency greater than or equal to minsup:' % len(values_freq))
    print(sorted(values_freq))
    
if __name__ == '__main__':
    
    f = open(file_name, 'r')
    dict_set = {}
    for tids, line_items in enumerate(f):
           dict_set[tids] = [j for j in line_items.split(' ')
                           if j != '\n']
            
    database = create_database(dict_set)
    try:
        charm_alg(3000)
        charm_alg(5000)
    except:
        print('Filename or support value is missing..')