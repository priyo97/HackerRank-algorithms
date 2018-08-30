def main():
    n = int(input())
    print(fact(n))
    

def fact(n):
    
    prod = n
    n -= 1
    
    while n > 1:
        prod *= n
        n -= 1
    
    return prod

main()
