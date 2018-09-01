def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    
    m = n + 1
    
    for i in range(n):
        for j in range(i+1,n):
            
            if a[i] == a[j]:
                d = j-i
                if d < m:
                    m = d
    
    if m == n+1:
        print(-1)
    else:
        print(m)
        
main()
    
