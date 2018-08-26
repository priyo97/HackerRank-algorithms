def main():
    
    n = int(input())
    a = [int(x) for x in input().split()]
    
    d = [0]*101
    for i in a:
        d[i] += 1
    
    max = 0
    for i in range(1,101):
        c = d[i] + d[i-1]
        
        if c > max:
            max = c
    
    print(max)
    

main()
        
        
