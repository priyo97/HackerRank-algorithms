def main():
    pages = int(input())
    no = int(input())
    
    count1 = 0
    count2 = 0
    
    for c in range(1,pages+1):
        if c == no:
            break
        
        if c % 2:
            count1 += 1
            
    for c in range(pages,0,-1):
        if c == no:
            break
        
        if not c % 2:
            count2 += 1
            
    if count1 < count2:
        print(count1)
    else:
        print(count2)
        
main()
        
