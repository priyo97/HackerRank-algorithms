def main():
    
    t = int(input())
    
    while t:
        
        m = int(input())
        n = int(input())
        
        a = [int(x) for x in input().split()]
        
        for i in range(n):
            for j in range(i+1,n):
                
                if a[i] + a[j] == m:
                    print(i+1,j+1)
                    
        t -= 1
        
main()
