def main():
    
    s = list(input())
    t = list(input())
    
    k = int(input())
    
    n = len(t)
    m = len(s)
    
    count = 0
    
    idx = 0
    
    for i in range(n):
        
        if idx < m and t[i] != s[idx]:
            count += m - idx
            count += n - i
            break
        elif idx == m:
            count += n - i
            
        idx += 1
    
    i += 1
    
    if i == n and n < m:
        count += m - i
    
    if count <= k:
        print("Yes")
    else:
        print("No")
        
main()
        
    
        
        
        
        
        
        
