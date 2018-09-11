def main():
    
    p = int(input())
    
    while p:
        
        s = set(input())
        t = set(input())
        
        if s & t:
            print("YES")
        else:
            print("NO")
         
        p -= 1
        
main()
