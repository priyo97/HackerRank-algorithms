def main():
    t = int(input())
    
    while t:
        
        s = input()
        n = len(s)
        
        r = s[::-1]
        
        for i in range(1,n):
            
            if abs( ord(s[i]) - ord(s[i-1]) ) != abs( ord(r[i]) - ord(r[i-1]) ):
                print("Not Funny")
                break
        else:
            print("Funny")
            
        t -= 1
        
main()
