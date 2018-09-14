def main():
    
    n,k = [int(x) for x in input().split()]
    
    a = [[int(x) for x in input().split()] for _ in range(n)]
    
    b = filter(lambda x: x[1] == 0, a)
    c = list(filter(lambda x: x[1] == 1, a))
    c.sort(key=lambda x: x[0],reverse=True)

    # print(c)
    s = 0 
    for i in b:
        s += i[0]
    
    for i in c[:k]:
        s += i[0]    
    
    for i in c[k:]:
        s -= i[0]
        
    print(s)
    
main()
