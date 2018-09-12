from collections import Counter

def main():
    
    n = int(input())
    a = [int(x) for x in input().split()]
    
    m = int(input())
    b = [int(x) for x in input().split()]
    
    c = Counter(b)
    
    for i in a:
        c[i] -= 1
        
    for i in sorted(c):
        if c[i]:
            print(i,end=" ")
    
                
main()
