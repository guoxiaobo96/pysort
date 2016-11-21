sample=[4,1,3,2,16,9,31,10,14,8,7]
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

def heap_sort(sample):
    def max_heapify(heap,i):
        heap_size=len(heap)
        left=2*i+1
        right=2*i+2
        if left<heap_size and heap[left]>heap[i]:
            largest=heap[left]
            num=left
        else:
            largest=heap[i]

        if right<heap_size and heap[right]>largest:
            largest=heap[right]
            num=right
        else:
            largest=largest

        if largest!=heap[i]:
            heap[num]=heap[i]
            heap[i]=largest
            max_heapify(heap,num)


    def build_max_heap(heap):
        heap_size=len(heap)
        i=int(heap_size/2)-1
        while i>=0:
            max_heapify(heap,i)
            i-=1
        return(heap)

    def sort(heap):
        max_heap=build_max_heap(heap)
        i=len(max_heap)-1
        j=0
        temp=[]
        while j<=i:
            temp.append(max_heap[j])
            j+=1
        while i>0:
            max_heap[i]=temp[0]
            temp[0]=temp[i]
            temp=temp[:i]
            max_heapify(temp,0)
            i=i-1
        max_heap[0]=temp[0]
        return (max_heap)
        
    return sort(sample)

def quick_sort(sample):
    def partition(unparted,p,r):
        x=unparted[r]
        i=p-1
        j=p 
        while j<r:
            if unparted[j]<=x:
                i+=1
                temp=unparted[j]
                unparted[j]=unparted[i]
                unparted[i]=temp
            j+=1
        temp=unparted[r]
        unparted[r]=unparted[i+1]
        unparted[i+1]=temp
        return (i+1)

    def sort(unsorted,p,r):
        if p<r:
            q=partition(unsorted,p,r)
            sort(unsorted,0,q-1)
            sort(unsorted,q+1,r)
        return(unsorted)
    length=len(sample)-1
    return(sort(sample,0,length))

def counting_sort(sample): 
    temp=[]
    temp_result=[]
    length=len(sample)
    i,j,max=0,0,0
    while j<length:
        if sample[j]>max:
            max=sample[j]
        j+=1
    j=0
    while i<=max:
        temp.append(0)
        temp_result.append(0)
        i+=1
    while j<length:
        temp[sample[j]]+=1
        j+=1
    j=1
    while j<=max:
        temp[j]=temp[j]+temp[j-1]
        j+=1
    j=length-1
    while j>0:
        temp_result[temp[sample[j]]]=sample[j]
        temp[sample[j]]-=1
        j=j-1
    j=0
    result=[]
    while j<=max:
        if temp_result[j]!=0:
            result.append(temp_result[j])
        j+=1
    return(result)
print(counting_sort(sample))

