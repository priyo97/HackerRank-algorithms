def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    
    breads = 0
    for i in range(n-1):
        if a[i] % 2:
            a[i] += 1
            a[i+1] += 1
            breads += 2
    
    if a[-1]%2:
        print("NO")
    else:
        print(breads)
        
main()
