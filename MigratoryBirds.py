def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    
    birds = set(a)
    max1 = 0
    idx = 99999
    
    for b in birds:
        c = a.count(b)
        
        if c == max1:
            if b < idx:
                idx = b
        elif c > max1:
            max1 = c
            idx = b
    
    print(idx)
    
main()
        
