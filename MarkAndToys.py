def main():
    
    n,k = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    
    a.sort()
    
    count = 0
    
    for i in a:
        
        if i < k:
            count += 1
            k -= i
            
    print(count)
            
main()
