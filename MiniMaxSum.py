def main():
    a = [int(x) for x in input().split()]
    a.sort()
    print(sum(a[:4]),sum(a[1:]))
    
main()
