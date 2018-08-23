def main():
    n = int(input())
    
    a = [int(x) for x in input().split()]
    
    pos_count  = 0
    neg_count  = 0
    zero_count = 0
    
    for i in a:
        if i > 0:
            pos_count += 1
        elif i < 0:
            neg_count += 1
        else:
            zero_count += 1
    
    print("{:.6f}".format(pos_count/n))
    print("{:.6f}".format(neg_count/n))
    print("{:.6f}".format(zero_count/n))
    
main()
