def main():
    
    s = input()
    
    n = len(s)
    
    count = 0
    
    for i in range(n):
        
        if i % 3 == 0 or i % 3 == 2:
            if s[i] != "S":
                count += 1
        else:
            if s[i] != "O":
                count += 1
                
    print(count)
    
main()
