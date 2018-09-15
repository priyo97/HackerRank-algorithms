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
            
            min = a*(n-1)
            max = b*(n-1)
            
            for i in range(min,max+1,b-a):

                 print(i,end=" ")

            print()
            
        t -= 1
        
main()
            
