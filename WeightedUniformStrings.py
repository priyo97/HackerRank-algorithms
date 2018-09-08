def main():
    
    s = input()

    d = set()
    
    c = -1
    
    m = ord("a")
    
    for i in s:
        
        if i == c:
            count += 1
            d.add(count * p)
        else:
            c = i
            
            p = ord(c) - m + 1

            d.add(p)

            count = 1
                
    n = int(input())
    
    while n:
        
        q = int(input())
        
        if q in d:
            print("Yes")
        else:
            print("No")
        
    
        n -= 1
        
main()
