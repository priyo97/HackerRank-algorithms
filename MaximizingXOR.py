def main():
    
    l = int(input())
    r = int(input())
    
    max = 0
    for i in range(l,r+1):
        for j in range(l,r+1):
            c = i ^ j
            
            if c > max:
                max = c
                
    print(max)
    
main()
