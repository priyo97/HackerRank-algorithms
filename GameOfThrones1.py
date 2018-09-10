from collections import Counter

def main():
    
    s = input()
    
    t = Counter(s)
    
    count = 0
    
    for i in t:
        
        if t[i] % 2:
            count += 1
            
    if count <= 1:
        print("YES")
    else:
        print("NO")
        
main()
    
    
