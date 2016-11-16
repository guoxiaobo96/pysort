sample=[2,7,5,6,2,4,10,1,3]
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
    def merge(left,right):
        result=[]
        left_length=len(left)
        right_length=len(right)
        i,j=0,0
        while i<left_length and j<right_length:
            if left[i]>right[j]:
                result.append(right[j])
                j+=1
            else:
                result.append(left[i])
                i+=1
        result+=left[i:]
        result+=right[j:]
        return (result)
    
    def merge_process(unmerged_list):
        if len(unmerged_list)<=1:
            return (unmerged_list)
        middle=int(len(unmerged_list)/2)
        left=merge_process(unmerged_list[:middle])
        right=merge_process(unmerged_list[middle:])
        return(merge(left,right))

    return(merge_process(sample))

print(merge_sort(sample))

