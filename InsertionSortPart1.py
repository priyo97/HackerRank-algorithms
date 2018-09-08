def main():
    
    n = int(input())
    
    a = [int(x) for x in input().split()]
    
    c = a[-1]
    
    for i in range(n-2,-1,-1):
        if a[i] > c:
            a[i+1] = a[i]
            print(" ".join(map(str,a)))

        else:
            a[i+1] = c
            print(" ".join(map(str,a)))
            break
    else:
        a[0] = c
        print(" ".join(map(str,a)))
            
main()
    
