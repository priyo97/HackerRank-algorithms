def main():
    
    t = int(input())
    
    while t:
        
        s = input()
        
        n = len(s)
        
        count = 0
        
        for i in range(n):
            if i < n - i - 1:
                if s[i] != s[n-i-1] :
                    c = abs( ord(s[i]) - ord(s[n-i-1]) )
                    count += c
        
        print(count)
                    
                    
        t -= 1
        
main()
