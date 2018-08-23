def main():
    n = int(input())
    a = [[int(x) for x in input().split()] for _ in range(n)]
    
    diag1 = 0
    diag2 = 0
    j = 0
    
    for i in a:
        diag1 += i[j]
        diag2 += i[n-1-j]
        j += 1
    
    print(abs(diag1-diag2))
    
main()
        
        
