def main():
    
    s = input().lower()
    
    a = [0]*26
    
    for i in s:
        
        if i != " ":
            a[ord(i)-ord("a")] = 1
    
    if sum(a) == 26:
        print("pangram")
    else:
        print("not pangram")

main()
    
