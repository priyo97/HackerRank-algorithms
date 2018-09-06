def main():
    
    n,m = [int(x) for x in input().split()]
    a = {int(x) for x in input().split()}
    
    d1 = [None]*n
    
    for j in range(n):
        if j in a:
            d1[j] = 0
        else:
            if j == 0:
                d1[j] = 10**9
            else:
                d1[j] = d1[j-1] + 1
    
    d2 = [None]*n
    
    for j in range(n-1,-1,-1):
        if j in a:
            d2[j] = 0
        else:
            if j == n-1:
                d2[j] = 10**9
            else:
                d2[j] = d2[j+1] + 1
    
    d = 0
    for i,j in zip(d1,d2):
        d = max(d,min(i,j))
                
    print(d)
    
main()
