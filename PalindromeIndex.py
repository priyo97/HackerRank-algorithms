def main():
    
    t = int(input())
    
    while t:
        
        s = input()
        
        n = len(s)

        i = 0                
        while i < n//2:

            if s[i] != s[n-i-1]:
                p = s[:i] + s[i+1:]
                q = s[:n-i-1] + s[n-i:]
                
                r = p[::-1]
                
                if p == r:
                    print(i)
                    break
                    
                r = q[::-1]
                if q == r:
                    print(n-i-1)
                    break
                    
            i += 1

        else:
            print(-1)
            
        t -= 1
        
main()
