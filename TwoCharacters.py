def main():

    n = int(input())
    string = list(input())
    
    d = list(set(string))
    l = len(d)
    
    chosen = set()
    
    permutation(d,l,chosen,2,string,n)
    
    print(m)

m = 0

def permutation(d,a,chosen,n,s,l):
    global m
    
    if n == 0:       
        t = []
        for i in s:
            if i in chosen:
                t.append(i)
                continue
            l -= 1
        
        for i in range(1,l):
            if t[i] == t[i-1]:
                return
        else:
            if l > m:
                m = l
       
    else:
        for i in range(a):
            c = d[i]
            d.remove(c)
            chosen.add(c)
            permutation(d,a-1,chosen,n-1,s,l)
            chosen.remove(c)
            d.insert(i,c)
            
main()
            
            
            
