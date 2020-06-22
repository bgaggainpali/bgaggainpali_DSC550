# File : BhargavaGaggainpali_DSC550_Week2_Exercise_Question4_3.4.1.py
# Name : Bhargava Gaggainpali
# Date : JUN-21-2020
# Course : DSC550 - Data Mining
# Assignment :Week2_Exercise_Question4_3.4.1


import matplotlib.pyplot as pyplt 

#r values = 3,6,5
#b values= 10,20,50
s_arr = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]

def calc_s_values(r, b):
    s = []
    for i in range(0,len(s_arr)):
        value=(1-(1-s_arr[i]**r)**b)
        s.append(value)
    return s

def plot(val_arr):
    x=s_arr
    y=val_arr
    pyplt.plot(x,y)
    pyplt.xlabel('S_Values')
    pyplt.ylabel("S_Curve_Values")
    pyplt.title("S_Value Vs S_Curve Plot")

if __name__ == '__main__':
     # try block for execution
    try:
        first_curve=calc_s_values(3,10)
        sec_curve=calc_s_values(6,20)
        third_curve=calc_s_values(5,50)
        # Plot curves using s_arr values
        plot(first_curve)
        plot(sec_curve)
        plot(third_curve)
        print("Plotted the curves successfully.")
    except Exception as exception:
        print('exception')
        print('An exception of type {0} occurred.  Arguments:\n{1!r}'.format(type(exception).__name__, exception.args));