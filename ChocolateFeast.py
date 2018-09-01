def main():
    t = int(input())
    
    while t:
        n,c,m = [int(x) for x in input().split()]
        
        count = n // c
        
        p = count
        
        while p >= m:
            count += p // m
            p = p % m + p // m
        
        print(count)
        
        t -= 1

main()
