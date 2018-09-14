def main():
    
    n = int(input())
    a = [int(x) for x in input().split()]
    
    a.sort(reverse=True)
    
    b = [ c*2**j for j,c in enumerate(a)]
    
    print(sum(b))
    
main()
