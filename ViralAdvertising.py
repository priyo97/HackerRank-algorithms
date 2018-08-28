def main():
    
    n = int(input())
    p = 5
    cumm = 0
    
    while n:
        
        c = p//2
        cumm += c
        p = c*3
        
        n -= 1
    
    print(cumm)
    
main()
    
