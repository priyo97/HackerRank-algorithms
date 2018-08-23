def main():
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    
    a_points = 0
    b_points = 0
    
    for i,j in zip(a,b):
        if i > j:
            a_points += 1
        elif j > i:
            b_points += 1
    
    print(a_points,b_points)
    
main()
            
