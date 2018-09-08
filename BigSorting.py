import functools

def compare(a,b):
    
    n = len(a)
    m = len(b)
    
    if n < m:
        return -1
    
    elif n == m:
        
        for i,j in zip(a,b):
            if i < j:
                return -1
            elif i > j:
                return 1
        else:
            return -1
    else:
        return 1
    
def main():
    
    n = int(input())
    
    a = []
    while n:
        a.append(input())
        n -= 1
    
    a = sorted(a,key=functools.cmp_to_key(compare))

    for i in a:
        print(i)
    
main()
        
    
