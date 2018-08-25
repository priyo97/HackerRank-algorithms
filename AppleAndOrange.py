def main():
    s,t = [int(x) for x in input().split()]
    a,b = [int(x) for x in input().split()]
    m,n = [int(x) for x in input().split()]
    
    apples = [int(x) for x in input().split()]
    oranges = [int(x) for x in input().split()]
    
    for i in range(m):
        apples[i] += a
    
    for i in range(n):
        oranges[i] += b
        
    count1 = 0
    count2 = 0
    
    for a in apples:
        if s <= a <= t:
            count1 += 1
    
    for o in oranges:
        if s <= o <= t:
            count2 += 1
            
    print(count1)
    print(count2)

main()
            
    
    
