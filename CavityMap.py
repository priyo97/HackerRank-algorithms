def main():
    
    n = int(input())
    
    a = [input() for _ in range(n)]
    
    if len(a[0].split()) == 1:
        flag = 1
    else:
        flag = 0
    
    for i in range(n):
        a[i] = [int(x) for x in "".join(a[i].split())]
    
    count = 0
    
    s = set()
    for i in range(1,n-1):
        for j in range(1,n-1):

            if a[i][j] > a[i+1][j] and a[i][j] > a[i-1][j]:
                if a[i][j] > a[i][j+1] and a[i][j] >a[i][j-1]:
                    s.add((i,j)) 
    
    
    
    if flag:
        for i in range(n):
            for j in range(n):
                if (i,j) in s:
                    print("X",end="")
                else:
                    print(a[i][j],end="")
            print()
    else:
        for i in range(n):
            for j in range(n):
                if (i,j) in s:
                    print("X",end=" ")
                else:
                    print(a[i][j],end=" ")
            print()
        
main()
