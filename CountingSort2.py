def main():
    
    n = int(input())
    
    a = [int(x) for x in input().split()]
    
    d = {}
    
    m = 0
    
    for i in a:
        
        d[i] = d.get(i,0) + 1
        if i > m:
            m = i
        
    for i in range(m+1):
        if i in d:
            for _ in range(d[i]):
                print(i,end=" ")
            
main()
