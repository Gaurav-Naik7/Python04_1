
def gfilter(methodtorun,data):
    elist=[]
    for i in range(len(data)):
        if methodtorun(data[i]):
            elist.append(data[i])
    return elist

def gmap(methodtorun,data):
    elist=[]
    for i in range(len(data)):
        data[i]=methodtorun(data[i])
        elist.append(data[i])
    return elist

def greduce(methodtorun,data):
    c=len(data)-1
    i=1
    var=methodtorun(data[0],data[1])
    while i<c:
        ans=methodtorun(var,data[(i+1)])
        var=ans
        i=i+1
    return var
