def checkrow(a,j,n):
    
    for i in range(1,n):
        if a[i][j] < a[i-1][j]:
            return False
    else:
        return True
        

def main():
    
    t = int(input())
    
    while t:
        
        n = int(input())
        
        a = [list(input()) for _ in range(n)]
        
        for i in a:
            i.sort()
        
        m = len(a[0])
        
        for j in range(m):
            if not checkrow(a,j,n):
                print("NO")
                break
        else:
            print("YES")
            
        t -= 1
        
main()
