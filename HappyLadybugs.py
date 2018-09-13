def main():
    
    t = int(input())
    
    while t:
        
        n = int(input())
        
        a = input()
        b = list(a)
        
        b.sort()
        
        # print(b)
        
        if b[-1] == "_":
            
            c = -1
            count = 0
            
            i = 0
            
            while c != "_":
                
                if c == b[i]:
                    count += 1
                else:
                    if count == 1:
                        print("NO")
                        break
                    else:
                        c = b[i]
                        count = 1

                i += 1
            else:
                print("YES")
        
        else:
            c = -1
            count = 0
           
            for i in range(n):
                if c == a[i]:
                    count += 1
                else:
                    if count == 1:
                        print("NO")
                        break
                    else:
                        c = a[i]
                        count = 1
            else:
                if count == 1:
                    print("NO")
                else:
                    print("YES")
                
        t -= 1
                
main()
        
