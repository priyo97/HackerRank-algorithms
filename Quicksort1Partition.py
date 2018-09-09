def main():
    
    n = int(input())
    a = [int(x) for x in input().split()]
    
    d = {"left":[],"equal":[],"right":[]}
    
    p = a[0]
    
    d["equal"].append(p)
    
    for i in a[1:]:
        
        if i < p:
            d["left"].append(i)
        elif i > p:
            d["right"].append(i)
        else:
            d["equal"].append(i)
            
    for i in ["left","equal","right"]:
        print(" ".join( map(str,d[i]) ),end=" ")

main()
