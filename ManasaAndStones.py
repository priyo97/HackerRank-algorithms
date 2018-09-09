def main():
    
    t = int(input())
    
    while t:
        
        n = int(input())
        a = int(input())
        b = int(input())
        
        if a == b:
            print((n-1)*a)
        else:
            
            if a > b:
                a,b = b,a
                
            for i in range(n):

                 print( a*(n-1-i) + b*i ,end=" ")

            print()
            
        t -= 1
        
main()
            
