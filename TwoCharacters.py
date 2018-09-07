def main():

    n = int(input())
    string = list(input())
    
    d = list(set(string))
    l = len(d)
    
    m = 0
    for i in range(l):
        for j in range(i+1,l):
            
            s = n
            t = []
            for k in string:
                if k == d[i] or k == d[j]:
                    t.append(k)
                    continue
                s -= 1
                
            for k in range(1,s):
                if t[k] == t[k-1]:
                    break
            else:
                if s > m:
                    m = s
            
    print(m)

main()
            
