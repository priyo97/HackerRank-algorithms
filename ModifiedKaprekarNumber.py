def main():
    p = int(input())
    q = int(input())
    
    flag = False
    
    for i in range(p,q+1):
        d = len(str(i))
        c = str(i ** 2)
        e = c[:-d] or "0"
        
        if i == int(c[-d:]) + int(e):
            print(i,end=" ")
            flag = True
    
    if not flag:
        print("INVALID RANGE")
        
main()
        
