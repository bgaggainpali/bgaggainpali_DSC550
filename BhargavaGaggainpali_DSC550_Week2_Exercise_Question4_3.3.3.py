# File : BhargavaGaggainpali_DSC550_Week2_Exercise_Question4_3.3.3.py
# Name : Bhargava Gaggainpali
# Date : JUN-21-2020
# Course : DSC550 - Data Mining
# Assignment :Week2_Exercise_Question4_3.3.3

import sys

ele_list = [0,1,2,3,4,5]
s1 = (0,0,1,0,0,1)
s2 = (1,1,0,0,0,0)
s3 = (0,0,0,1,1,0)
s4 = (1,0,1,0,1,0)

def hash1(a):
    return ((2 * a) + 1) % 6
def hash2(a):
    return ((3 * a) + 2) % 6
def hash3(a):
    return ((5 * a) + 2) % 6

def hash_1(ele_list):
    hash_list = []
    for i in ele_list:  
        val=hash1(i)
        hash_list.append(val)
    return hash_list
def hash_2(ele_list):
    hash_list = []
    for i in ele_list:      
        val=hash2(i)
        hash_list.append(val)
    return hash_list    
def hash_3(ele_list):
    hash_list = []
    for i in ele_list:    
        val=hash3(i)
        hash_list.append(val)
    return hash_list

def PermutCheck(hash_name, hash_list):
    hash_list.sort()
    ele_list.sort()
    if hash_list == ele_list:
        print(hash_name + ' is a true permutation of elements list')
    else:
        print(hash_name + ' is not a true permutation of elements list')


# function to compute intersection of two lists
def intersection_cardinality(a,b):
    return len(list(set(a).intersection(b)))

# function to compute union of two lists
def union_cardinality(a,b):
    return (len(a) + len(b)) - intersection_cardinality(a,b)       

# Compute Jaccard similarity of two lists
def jaccard_similarity(a,b):
    # Intersection of two lists
    inter = len(list(set(a).intersection(b)))
    # Union of two lists
    union = (len(a) + len(b)) - intersection_cardinality(a,b)
    return round(float(inter) / union,3)
 
# function to reverse columns and rows within the ss, filling a single list
def s_data():
    hold_matrix = []
    length=len(s1)
    for i in range(0, length):
        hold_matrix.append([s1[i], s2[i], s3[i], s4[i]])
    return hold_matrix

# Minhash signature code
def minhash(data, hashfuncs):
    row = len(data)
    col = len(data[0])
    sigrow = len(hashfuncs)
    sig_mat = []
    for i in range(sigrow):
        sig_mat.append([sys.maxsize] * col)
    for r in range(row):
        val = list(map(lambda a: a(r), hashfuncs))
        # if data != 0 and signature > hash value, replace signature with hash value
        for c in range(col):
            if data[r][c] == 0:
                continue
            for i in range(sigrow):
                # if the sigmatrix value is greater than the hashvalue, replace with hashvalue
                if sig_mat[i][c] > val[i]:
                    sig_mat[i][c] = val[i]
    return sig_mat 
if __name__ == '__main__':
    try:        
        # Compute minhash signature values
        print('\n(1) Compute the minhash signature for each column using three hash functions.')
        sig_data = minhash(s_data(), [hash1, hash2, hash3])
        print('\n Minhash Signature Values: \n' + str(sig_data))
        
        # second question
        print('\n(2) Which of these hash functions are true permutations?')
        PermutCheck('\nHash 1', hash_1(ele_list))
        PermutCheck('Hash 2', hash_2(ele_list))
        PermutCheck('Hash 3', hash_3(ele_list))
        
        #comparing estimated Jaccard similarities
        # Third questions
        print('\n(3) How close are the estimated Jaccard Similarities to the true Jaccard Similarities?')
        # similarities of 6 pairs of columns
        print('\nSimilarities in s1 and s2:', str(jaccard_similarity(s1, s2)))
        print('Similarities in s1 and s3:', str(jaccard_similarity(s1, s3)))
        print('Similarities in s1 and s4:',str(jaccard_similarity(s1, s4)))
        print('Similarities in s2 and s3:',str(jaccard_similarity(s2, s3)))
        print('Similarities in s2 and s4:',str(jaccard_similarity(s2, s4)))
        print('Similarities in s3 and s4:',str(jaccard_similarity(s3, s4)))
         
        # similarities of signatures 
        # establish columns of signatures
        minhash_1 = [sig_data[0][0], sig_data[1][0], sig_data[2][0]]
        minhash_2 = [sig_data[0][1], sig_data[1][1], sig_data[2][1]]
        minhash_3 = [sig_data[0][2], sig_data[1][2], sig_data[2][2]]
        minhash_4 = [sig_data[0][3], sig_data[1][3], sig_data[2][3]]
        
        # similarities of signatures 1 & 2, 1 & 3, 1 & 4, 2 & 3, 2 & 4, 3 & 4
        print('\nSignature similarity in 1 and 2: ',str(jaccard_similarity(minhash_1, minhash_2)))
        print('Signature similarity in 1 and 3: ',str(jaccard_similarity(minhash_1, minhash_3)))
        print('Signature similarity in 1 and 4: ',str(jaccard_similarity(minhash_1, minhash_4)))
        print('Signature similarity in 2 and 3: ',str(jaccard_similarity(minhash_2, minhash_3)))
        print('Signature similarity in 2 and 4: ',str(jaccard_similarity(minhash_2, minhash_4)))
        print('Signature similarity in 3 and 4: ', str(jaccard_similarity(minhash_3, minhash_4)))
    
        print('\nThe estimated Jaccard similarities are not close to the true Jaccard similarities.')
    except Exception as exception:
        print('An exception of type {0} occurred.  Arguments:\n{1!r}'.format(type(exception).__name__, exception.args));    