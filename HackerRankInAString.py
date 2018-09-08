def main():
    
    t = int(input())
    
    d = "hackerrank"
    
    while t:
        
        s = input()
        
        k = 0
        
        for i in s:
            
            if d[k] == i:
                k += 1
            
            if k == 10:
                print("YES")
                break
        else:
            print("NO")
        
        t -= 1
        
main()
