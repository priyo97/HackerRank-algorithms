def main():
    
    n,m = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    
    while m:
      
        i,j = [int(x) for x in input().split()]
        print(min(a[i:j+1]))
        
        m -= 1
    
main()
