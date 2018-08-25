def main():
    n = int(input())
    c = [int(x) for x in input().split()]
    
    d,m = [int(x) for x in input().split()]
    
    count = 0
    
    for i in range(n-m+1):
        if d == sum(c[i:i+m]):
            count += 1
            
    print(count)
    
main()
