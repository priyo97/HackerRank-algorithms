def main():
    n = int(input())
    s = input()
    
    sea_level = True
    count = 0
    
    v = 0
    
    for i in s:
        if i == "D":
            count -= 1
        else:
            count += 1
        
        if sea_level and count < 0:
            v += 1
            sea_level = False
        elif count == 0:
            sea_level = True
    
    print(v)
    
main()
            
