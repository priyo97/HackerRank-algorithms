def main():
    
    t = int(input())
    
    c = 3
    i = 1
    
    while True: 
        
        if t <= i+c-1:
            c = c - (t-i)
            break
        else:
            i = i+c
            c = c * 2
    
    print(c)
    
main()
