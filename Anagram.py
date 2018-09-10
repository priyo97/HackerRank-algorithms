def main():
    
    t = int(input())
    
    while t:
        
        s = input()
        n = len(s)
        
        if n % 2 :
            print(-1)
        else:
            p = s[:n//2]
            q = s[n//2:]
            
            r = list(q)
            count = 0
            for i in p:
                
                if i in r:
                    count += 1
                    r.remove(i)
                    
            print(n//2 - count)
            
        t -= 1
        
main()
