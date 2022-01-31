from modulefmr import gfilter
from modulefmr import gmap
from modulefmr import greduce

def CheckEven(no):
    if(no%2==0):
        return True
    else:
        return False
    #return (no%2==0)

def Increment(no):
    return no+2

def main():
    data=[5,7,6,8,4,7,6]
    print("Original data is",data)

    newData=list(gfilter(CheckEven,data))
    print("Filtered data is",newData)

    incrementdata=list(gmap(Increment,newData))
    print("Data after map",incrementdata)

    ret=greduce(lambda a,b:a+b,incrementdata)
    print("Data after reduce ",ret)

if __name__=="__main__":
    main()
