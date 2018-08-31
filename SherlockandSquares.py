def main():

    import math
    
    t = int(input())
    
    while t:
        
        l,h = [int(x) for x in input().split()]
        
        b = math.floor(math.sqrt(h))
        a = math.ceil(math.sqrt(l))
        
        print(b-a+1)
        
        t -= 1

main()
    
