def main():
    t = int(input())
    while t:
        
        n,k = [int(x) for x in input().split()]
        a = [int(x) for x in input().split()]
        
        count = 0
        
        for i in a:
            if i <= 0:
                count += 1
                
        if count >= k:
            print("NO")
        else:
            print("YES")
        
        t -= 1
        
main()
        
