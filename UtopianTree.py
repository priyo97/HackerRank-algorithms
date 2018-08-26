def main():
    t = int(input())
    
    while t:
        
        h = 1
        n = int(input())
        
        for i in range(n):
            if i % 2 == 0 :
                h *= 2
            else:
                h += 1
                
        print(h)
        
        t -= 1

main()
