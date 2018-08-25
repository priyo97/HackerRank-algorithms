def main():
    n = input()
    scores = [int(x) for x in input().split()]
    
    max1 = scores[0]
    min1 = scores[0]
    
    count1 = 0
    count2 = 0
    
    for s in scores[1:]:
        if s > max1:
            count1 += 1
            max1 = s
        elif s < min1:
            count2 += 1
            min1 = s
            
    print(count1,count2)
    
main()
