def main():
    
    n = int(input())
    
    a = [int(x) for x in input().split()]
    
    a.sort()
    
    min = 99999999999
    
    for i in range(1,n):
        c = abs(a[i]-a[i-1])
        if c < min:
            min = c
            
    print(min)
    
main()
