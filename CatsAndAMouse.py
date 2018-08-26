def main():
    t = int(input())
    
    while t:
        x,y,z = [int(x) for x in input().split()]
        
        d1 = abs(z - x)
        d2 = abs(z - y)
        
        if d1 == d2:
            print("Mouse C")
        elif d1 < d2:
            print("Cat A")
        else:
            print("Cat B")
        
        t -= 1      

main()
