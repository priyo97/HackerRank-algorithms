def main():
    
    n = int(input())
    
    s = list(input())
    
    count = 0
    
    for i in range(2,n):
        
        if s[i-2:i+1] == ["0","1","0"]:
            count += 1
            s[i] = 1
            
    print(count)
    
main()
