def main():
    i,j,k = [int(x) for x in input().split()]
    
    count = 0
    
    for t in range(i,j+1):
        s = int(str(t)[::-1])
        
        if abs(t-s) % k == 0:
            count += 1
    
    print(count)

main()
        
