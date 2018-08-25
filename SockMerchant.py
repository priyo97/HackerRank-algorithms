def main():
    n = int(input())
    socks = [int(x) for x in input().split()]
    
    s = set(socks)
    
    count = 0
    
    for i in s:
        count += socks.count(i)//2
    
    print(count)
    
main()
