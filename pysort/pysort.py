sample=[5,2,4,1,3,6]
def insert_sort(smaple):
    result=[smaple[0]]
    j=1
    while j<len(sample):
        key=sample[j]
        i=j-1
        result.append(0)
        while i>=0 and result[i]>key:
            result[i+1]=result[i]
            i=i-1
        result[i+1]=key
        j=j+1
    return(result)

def merge_sort(sample):
    length=len(sample)
    middle=length/2
    i=0
    j=int(middle)
    k=0
    left=[]
    right=[]
    result=[]
    while i < middle:
        left.append(sample[i])
        i=i+1
    left.append(10000)
    while j<length :
        right.append(sample[j])
        j=j+1
    right.append(10000)
    i=0
    j=0
    while k<length:
        if left[i]>right[j]:
            result.append(right[j])
            j=j+1
        else:
            result.append(left[i])
            i=i+1
        k=k+1
    return (result)
print(merge_sort(sample))

