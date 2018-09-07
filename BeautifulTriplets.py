def main():
    n,d = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    
    count = 0
    
    for i in range(n):
        for j in range(i+1,n):
            
            if a[j] - a[i] == d:
                for k in range(j+1,n):

                    if a[k] - a[j] == d:
                        count += 1
                    elif a[k] - a[j] > d:
                        break
            
            elif a[j] - a[i] > d:
                break
    
    print(count)
    
main()
