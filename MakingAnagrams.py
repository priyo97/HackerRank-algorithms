from collections import Counter

def main():
    
    s = input()
    t = input()
    
    p = Counter(s)
    q = Counter(t)
    
    k = p.keys() & q.keys()
    
    count = 0
    for i in k:
        count += abs(p[i] - q[i])
    
    for i in p:
        if i not in k:
            count += p[i]
    
    for i in q:
        if i not in k:
            count += q[i]
            
            
    print(count)
    
main()
    
    
        
    
    
    
