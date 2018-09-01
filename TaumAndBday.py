def main():
    
    t = int(input())
    
    while t:
        b,w = [int(x) for x in input().split()]
        bc,wc,z = [int(x) for x in input().split()]
        
        if bc < wc:
            c = bc + z
            if c < wc:
                c = c*w
            else:
                c = wc*w
                
            tc = bc*b + c
        else:
            c = wc + z
            
            if c < bc:
                c = c*b
            else:
                c = bc*b
            
            tc = wc*w + c
        
        print(tc)
        
                
        t -= 1
        
main()
