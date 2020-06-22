# File : BhargavaGaggainpali_DSC550_Week2_Exercise_Question4_3.2.1.py
# Name : Bhargava Gaggainpali
# Date : JUN-21-2020
# Course : DSC550 - Data Mining
# Assignment :Week2_Exercise_Question4_3.2.1

# main function
if __name__ == '__main__':
    firstsentence='The most eﬀective way to represent documents as sets, for the purpose of identifying lexically similar documents is to construct from the document the set of short strings that appear within it.'
    #k value in k-shingles is given as 3
    k = 3  
    try:
        print('Given sentence is:', firstsentence, '\n')
        text = firstsentence.replace(',', '').split()
        print("First ten 3-shingles in given sentence:",'\n',str([text[x:x + k] for x in range(0, 10)]))
    except Exception as exception:
        print('An exception of type {0} occurred.  Arguments:\n{1!r}'.format(type(exception).__name__, exception.args));