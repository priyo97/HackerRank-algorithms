def main():
    
    n,k = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    
    count = 0
    
    for i in range(n):
        for j in range(i+1,n):
            if not (a[i]+a[j]) % k :
                count += 1
    
    print(count)

main()
