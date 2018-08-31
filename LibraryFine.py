def main():
    d1,m1,y1 = [int(x) for x in input().split()]
    d2,m2,y2 = [int(x) for x in input().split()]
    
    if y1 < y2:
        
        fine = 0
        
    elif y1 == y2:
        
        if m1 < m2:
            fine = 0
        elif m1 == m2:
            if d1 <= d2:
                fine = 0
            else:
                fine = 15 * (d1 - d2)
        else:
            fine = 500 * (m1 - m2)
    else:
        fine = 10000
    
    print(fine)
    
main()
            
