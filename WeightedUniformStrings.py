def main():
    
    s = input()
    
    n = len(s)

    d = {}
    
    i = 0
    
    while i < n:
        
        c = s[i]
        
        m = ord("a")
        
        p = ord(c) - m + 1
        
        d[p] = True
        
        count = 1
        
        j = i + 1
        
        while j < n:
            
            if s[j] == c:
                count += 1
                d[count * p] = True
            else:
                break
            
            j += 1
        
        i = j
        
    n = int(input())
    
    while n:
        
        q = int(input())
        
        if d.get(q,False):
            print("Yes")
        else:
            print("No")
        
    
        n -= 1
        
main()
