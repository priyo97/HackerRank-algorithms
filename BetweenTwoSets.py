def main():
    
    n,m = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    
    max1 = max(a)
    min1 = min(b)
    
    count = 0
    
    for i in range(max1,min1+1):
        for j in a:
            if i % j:
                break
        else:
            for j in b:
                if j % i:
                    break
            else:
                count += 1
    
    print(count)
    
main()    
