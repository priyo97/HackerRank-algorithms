def main():
    
    n = int(input())
    s = input()
    
    special_characters = "!@#$%^&*()-+"
    
    s1 = False
    s2 = False
    s3 = False
    s4 = False
    
    for i in s:
        
        if '0' <= i <= '9':
            s1 = True
        
        elif 'a' <= i <= 'z':
            
            s2 = True
        elif "A" <= i <= "Z":
            
            s3 = True
        
        elif i in special_characters:
            
            s4 = True
    
    if s1 and s2 and s3 and s4:
        if n >= 6:
            c = 0
        else:
            c = 6 - n
    else:
        c = (not s1) + (not s2) + (not s3) + (not s4)
        
        if n + c < 6:
            c += 6 - (c+n)
    
    print(c)
    
    
main()
