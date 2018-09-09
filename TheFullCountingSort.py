def main():
    
    n = int(input())
    
    m = n
    
    d = {}
    
    max = 0
    
    while m:
        
        t = input().split()
        i = int(t[0])
        
        if i > max:
            max = i
            
        if m > n//2:
            t[1] = "-"
        
        if i in d:
            d[i].append(t[1])
        else:
            d[i] = [t[1]]
        
        m -= 1
    
    for i in range(max+1):
        if i in d:
            for k in d[i]:
                print(k,end=" ")
                
main()
    
    
