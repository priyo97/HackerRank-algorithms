def main():
    
    n = int(input())
    
    d = {}
    
    for i in input().split():
        i = int(i)
        d[i] = d.get(i,0) + 1
    
    m = max(d,key=lambda x: d[x])
    
    count = 0
    
    for i in d:
        
        if i != m:
            count += d[i]
            
    print(count)
    
main()
        
