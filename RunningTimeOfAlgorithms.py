def main():
    
    n = int(input())
    a = [int(x) for x in input().split()]
    
    count = 0
    for i in range(1,n):
        
        c = a[i]

        for j in range(i-1,-1,-1):
            
            if a[j] > c:
                a[j+1] = a[j]
                count += 1
                
            elif a[j] <= c:
                a[j+1] = c
                break
        else:
            a[j] = c
    
    print(count)
    
main()
        
