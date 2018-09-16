def main():
    
    n = int(input())
    a = [int(x) for x in input().split()]
    
    a.sort()
    
    count = 0
    c = a[0]
    
    for i in range(1,n):
        if a[i] > c + 4:
            count += 1
            c = a[i]
            
    print(count+1)
    
main()
        
