sample=[5,2,4,6,1,3]
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
    pass
print(insert_sort(sample))

