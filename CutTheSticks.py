def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    
    while a:
        
        print(len(a))
        m = min(a)
        while m in a:
            a.remove(m)
        a = [i - m for i in a]

main()
            
