def main():
    
    n,k = [int(x) for x in input().split()]
    heights = [int(x) for x in input().split()]
    
    m = max(heights)
    
    if m < k:
        print(0)
    else:
        print(m-k)
    
main()
