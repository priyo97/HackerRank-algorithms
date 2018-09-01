def main():
    
    n,m = [int(x) for x in input().split()]
    l = []
    
    for _ in range(n):
        
        d = [int(x) for x,y in enumerate(input()) if y == "1"]
        l.append(d)
    
    m = 0
    count = 0
    
    d = []
    
    for i in range(n):
        for j in range(i+1,n):
            
            p = len(set(l[i]+l[j]))

            d.append(p)
            
    m = max(d)
    count = d.count(m)
                
    print(m)
    print(count)
    
main()
                
        
        
