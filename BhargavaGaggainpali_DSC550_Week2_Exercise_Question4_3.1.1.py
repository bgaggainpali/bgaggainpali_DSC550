# File : BhargavaGaggainpali_DSC550_Week2_Exercise_Question4_3.1.1.py
# Name : Bhargava Gaggainpali
# Date : JUN-21-2020
# Course : DSC550 - Data Mining
# Assignment :Week2_Exercise_Question4_3.1.1

#Example sets
A={1,2,3,4}
B={2,3,5,7}
C={2,4,6}

def calc_jaccard(set1, set2):
    s1 = set(set1)
    s2 = set(set2)
    return len(s1.intersection(s2)) / len(s1.union(s2))

# main function
if __name__ == '__main__':
     # calling function inside try block
    try:
        pair1=calc_jaccard(B,C)
        pair2=calc_jaccard(A,B)
        pair3=calc_jaccard(C,A)
        print("Jaccard similarity between B & C:",pair1)
        print("Jaccard similarity between A & B:",pair2)
        print("Jaccard similarity between C & A:",pair3)
        # values in percentages.
        print("Jaccard similarity inpercentage between B and C:",pair1*100)
        print("Jaccard similarity inpercentage between A and B:",pair2*100)
        print("Jaccard similarity inpercentage between C and A:",pair3*100)
    except Exception as exception:
        print('An exception of type {0} occurred.  Arguments:\n{1!r}'.format(type(exception).__name__, exception.args));