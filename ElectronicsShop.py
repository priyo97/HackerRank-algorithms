def main():
    b,n,m = [int(x) for x in input().split()]
    k = [int(x) for x in input().split()]
    u = [int(x) for x in input().split()]
    
    max_value = -1
    
    for i in k:
        for j in u:
            m = i + j
            if m <= b:
                if m > max_value:
                    max_value = m
                    
    print(max_value)
    
main()
