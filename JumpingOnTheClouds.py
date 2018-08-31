def main():
    
    n = int(input())
    a = [int(x) for x in input().split()]
    
    i = 0
    count = 0
    while True:
        
        if i < n - 2 and not a[i]:
            i += 2
        else:
            i += 1
            
        count += 1
        
        if i == n-1:
            break
            
    print(count)

main()
