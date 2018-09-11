def main():
    
    t = int(input())
    
    while t:
        
        s = input()
        print( len(set(s)) )
        t -= 1

main()
