def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    
    for x in range(1,n+1):
        for i in range(n):
            if x == a[i]:
                for j in range(n):
                    if i+1 == a[j]:
                        print(j+1)

main()
