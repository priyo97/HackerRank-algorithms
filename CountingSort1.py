def main():
    
    n = int(input())
    
    a = [int(x) for x in input().split()]
    
    d = {}
    
    for i in a:
        d[i] = d.get(i,0) + 1
    
    for i in range(100):
        if i in d:
            print(d[i],end=" ")
        else:
            print(0,end=" ")
main()
