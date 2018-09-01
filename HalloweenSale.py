def main():
    p,d,m,s = [int(x) for x in input().split()]
    
    count = 0
    
    while s > 0:
        
        if p <= s:
            count += 1
            s = s - p
        else:
            break
            
        if p - d  > m:
            p = p - d
        else:
            p = m
            
    print(count)
    
main()
