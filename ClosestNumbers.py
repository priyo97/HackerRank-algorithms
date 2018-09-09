def main():
    
    n = int(input())
    a = [int(x) for x in input().split()]
    
    n = len(a)
    a.sort()
    
    m = 99999999

    for i in range(1,n):
        t = abs(a[i] - a[i-1])
        
        if t < m:
            m = t
            d = [a[i-1],a[i]]
            
        elif t == m:
            
            d.extend([a[i-1],a[i]])
                      
    for i in d:
        print(i,end=" ")
                      
main()
            
            
