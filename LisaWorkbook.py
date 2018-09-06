def main():
    
    n,k = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    
    page = 1
    count = 0
    
    for problems in a:
        for i in range(1,problems+1):
            if i == page:
                count += 1
            
            if i % k == 0 or i == problems:
                page += 1
    
    print(count)
    
main()
    
        
