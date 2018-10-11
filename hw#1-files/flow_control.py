#define a function
def flow_control(k):

    #define a string based ont he value of k
    if(k==0):
        s = "Variable k = %d equals 0." % d
    
    elif(k==1):
        s = "Variable k = %d equals 1." % d

    else:
        s = "Variable k = %d does not equal 0 or 1." % k

#print the varible
print(s)

#define a main function
def main():

    #delcrae an interger
    i = 0

    #try flow_control for 0,1,2
    flow_control(i)
    i = 1
    flow_control(i)
    i = 2
    flow_control(i)

#run the program
if __name_ == "__main__":
    main()
