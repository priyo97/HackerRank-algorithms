def main():
    
    n = int(input())
    
    r = []
    for _ in range(n):
        r.append(input())
        
    minerals = {x for i in r for x in i}
    
    count = 0
    
    for i in minerals:
        for j in r:
            if i not in j:
                break
        else:
            count += 1
            
    print(count)
    
main()
    
