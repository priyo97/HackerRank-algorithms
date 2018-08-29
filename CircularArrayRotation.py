def main():
    
    n,r,q = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    
    l = {(x+r) % n : a[x] for x in range(n)}
    
    while q:
        m = int(input())
        print(l[m])
    
main()
    
    
