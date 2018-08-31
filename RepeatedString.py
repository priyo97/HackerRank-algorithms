def main():
    
    s = input()
    n = int(input())
    
    m = len(s)
    
    count = 0
    
    for i in s:
        if i == "a":
            count += 1
    
    k = n // m
    
    count = k * count
    
    q = n % m
    
    for i in s[:q]:
        if i == "a":
            count += 1
    
    print(count)
    
main()
    
    
