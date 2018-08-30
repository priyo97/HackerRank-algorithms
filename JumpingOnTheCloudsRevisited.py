def main():
    
    n,k = [int(x) for x in input().split()]
    c = [int(x) for x in input().split()]
    
    e = 100
    i = 0
    
    i = ( i + k ) % n
    e -= 1
    
    if c[i] == 1:
        e -= 2
    
    while i:
        i = ( i + k ) % n
        e -= 1
    
        if c[i] == 1:
            e -= 2
    
    print(e)

main()
