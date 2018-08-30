def main():
    t = int(input())
    
    while t:
        
        n = int(input())
        
        s = [not n % int(d) for d in str(n) if int(d)]
        
        print(sum(s))
        
        t -= 1
        
main()
