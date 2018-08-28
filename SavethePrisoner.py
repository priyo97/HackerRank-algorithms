def main():
    
    t = int(input())
    
    while t:
        
        n,m,s = [int(x) for x in input().split()]
        
        c = n - s + 1
        
        m = m - c
        
        if m > 0:
            c = m % n
            if c == 0:
                print(n)
            else:
                print(c)
        else:
            print(n + m)
        
        
        t -= 1
        
main()
