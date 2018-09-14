def main():
    
    n = int(input())
    a = [int(x) for x in input().split()]
    
    d = {}
    for i in a:
        d[i] = d.get(i,0) + 1
        
    for i in d:
        if d[i] == 1:
            print(i)
            break
            
main()
    
