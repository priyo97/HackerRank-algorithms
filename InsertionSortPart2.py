def main():
    n = int(input())
    
    a = [int(x) for x in input().split()]
    
    for i in range(1,n):
        
        c = a[i]
        
        for j in range(i-1,-1,-1):
            
            if a[j] <= c:
                a[j+1] = c
                break
            else:
                a[j+1] = a[j]
        else:
            a[0] = c
            
        print(" ".join(map(str,a)))

main()
