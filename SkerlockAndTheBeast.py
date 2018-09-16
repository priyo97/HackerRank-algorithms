def main():
    
    t = int(input())
    
    while t:
      
        n = int(input())
        
        for i in range(n,-1,-1):
                
            if i % 3 == 0:
                if (n - i) % 5 == 0:
                    five = i
                    three = n - i
                    print("5"*five + "3"*three)
                    break
        else:
            print(-1)
                            
        t -= 1
        
main()
