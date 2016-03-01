q=0


def mergeSort(a):
    
    n=len(a)
    hi=len(a)-1
    lo=0
    if hi<=lo:
        return a
    else:

        mid=(hi+lo)//2
        b=a[:mid+1]
        c=a[mid+1:]
        mergeSort(b)
        mergeSort(c)
        merge(b,c,a) 
    return a

def merge(b,c,a):
        i=0
        j=0
        k=0
        
        while i<len(b) and j<len(c):
            
            if b[i][q]<=c[j][q]:
                a[k]=b[i]
                i+=1
                k+=1
            else:
                a[k]=c[j]
                j+=1
                k+=1
        while i<len(b):
            a[k]=b[i]
            i+=1
            k+=1
        while j<len(c):
            a[k]=c[j]
            j+=1
            k+=1
        return a
