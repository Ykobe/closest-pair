import point_pair
import mergesort
point1=(0,0)
point2=(0,0)
d = point_pair.point_distance(point1, point2)
l=100
def xsort(p):
    mergesort.q = 0
    
    mergesort.mergeSort(p)
    return p
def ysort(p):
    mergesort.q = 1
    mergesort.mergeSort(p)
    return p

def brute_force(r):
    if len(r)==2:
            point1= r[0]
            point2= r[1]
            
            return [point1,point2]
    else:
            x= point_pair.pair_distance([r[0],r[1]])
            y= point_pair.pair_distance([r[0],r[2]])
            z= point_pair.pair_distance([r[1],r[2]])
            if x<=y:
                if x<=z:
                    point1= r[0]
                    point2= r[1]

                    return [point1,point2]
                else:
                    point1= r[1]
                    point2= r[2]

                    return [point1,point2]
            else:
                if y<=z:
                    point1= r[0]
                    point2= r[2]

                    return [point1,point2]
                else:
                    point1= r[1]
                    point2= r[2]

                    return [point1,point2]
        


def closest_pair(p):
    s=[]
    w=[]
    for i in p:
        s.append(i)
        w.append(i)

    x=xsort(s)

    y=ysort(w)

    return cp (x)


def cp ( x):
    
    if (len(x)<=3):
        return brute_force(x)
    else:
        
        xL = xsort(x [:len(x)//2])
     
        xR = xsort (x [len(x)//2:])
     
        div = (x[len(x)//2-1][0]+ x[len(x)//2][0])/2

        t= []
        for i in x:
            t.append(i)
        
        y = ysort(t)

        a = cp (xL)
 
        f = point_pair.pair_distance(a)
        
        b = cp (xR)

        g = point_pair.pair_distance(b)
        
        if point_pair.pair_distance(a)>=point_pair.pair_distance(b):
            minlength = point_pair.pair_distance(b)
        else:
            minlength = point_pair.pair_distance(a) 
        return across_line (a,b, div,y, minlength)

def across_line (a,b, div,y, minlength):
        f = point_pair.pair_distance(a)
        
        g = point_pair.pair_distance(b)
        
        if f <= g:
           c = a
           u = div+f
           v = div -f
        else:
           c = b
           u = div+g
           v = div -g


        for i in range (len(y)):
            yprime = []
            if y[i][0]>=v and y[i][0]<=u:
                yprime.append(y[i])

        for j in yprime:
            if f <=g:
                m = j[1]-f
                n = j[1]+f
            else:
                m = j[1]-g
                n = j[1]+g
            for k in yprime:
                if k != j:
                    if k[1]>=m and k[1]<n:                      
                       
                       e =  point_pair.point_distance(j,k)
                       if e < f and e<g and e<minlength:
                          minlength = e                          
                          c = (j,k)
               
    
        return c          
