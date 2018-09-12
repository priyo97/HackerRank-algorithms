def main():
    
    n = int(input())
    
    l = []
    
    for i in range(n):
        
        l.append([i]+[sum([int(x) for x in input().split()])] )
        
    l.sort(key=lambda x : x[1])
    
    for i in l:
        print(i[0]+1,end=" ")
        
main()
        
    
        
    
