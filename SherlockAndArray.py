def main():
    
    t = int(input())
    
    while t:
        
        n = int(input())
        a = [int(x) for x in input().split()]
        
        if n == 1:
            print("YES")
        elif n == 2:
            print("NO")
        else:
            a = [0] + a            # test cases: 2 0 0 0 
            sum1 = sum(a[1:])
            sum2 = 0
            for i in range(1,n):
                
                sum1 -= a[i]
                sum2 += a[i-1]
                
                if sum1 == sum2:
                    print("YES")
                    break
            else:
                print("NO")
            
        t -= 1
        
main()
