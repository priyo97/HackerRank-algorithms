def main():
    
    n = int(input())
    while n:
        
        m = int(input())
        
        d = 5 - m % 5
        
        if d < 3 and m >= 38:
            print(m + d)
        else:
            print(m)
            
        n -= 1
        
main()
